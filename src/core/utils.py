import io
import re
import math
import unicodedata
import soundfile as sf
import torch
import torchaudio
from typing import Literal, Optional
from .schema import Word, Chunk
from configs.config import Config

EPS = Config.eps
WINDOW_SIZE = Config.window_size

#--------------------- Process audio ---------------------
def process_audio_bytes(
    audio_bytes, 
    source_format = None,
    target_channels = 1
    ):
    """
    return: (waveform, sample_rate, duration) or (None, None, None)
    """
    file_obj = io.BytesIO(audio_bytes)
    
    # Try soundfile (OGG/WAV)
    try:
        info = sf.info(file_obj)
        file_obj.seek(0)
        array, sr = sf.read(file_obj)
        # Convert to Tensor format and unify to (Channels, Time)
        waveform = torch.from_numpy(array).float()
        if waveform.ndim == 1:
            waveform = waveform.unsqueeze(0) # convert to single channel (1, T)
        else:
            waveform = waveform.t() # (T, C) -> (C, T)
        if waveform.shape[0] > 1 and target_channels == 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)
        return waveform, sr, info.duration
            
    except Exception:
        file_obj.seek(0) # reset pointer
        pass

    # try Torchaudio (support m4a, mp3)
    try:
        waveform, sr = torchaudio.load(file_obj, format=source_format)
        duration = waveform.shape[1] / sr
        
        if waveform.shape[0] > 1 and target_channels == 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)

        return waveform, sr, duration

            
    except Exception as e:
        return None, None, 0.0
#--------------------- Process audio ---------------------


#--------------------- NLP process ---------------------
def build_transcription_chunks(
        duration: float, 
        words: list[Word], 
        chunk_size: float = WINDOW_SIZE,
        eps: float = EPS
    ) -> list[Chunk]:
    chunks: list[Chunk] = []
    words_idx_start = 0
    n_windows = max(1, math.ceil(duration / chunk_size))
    for i in range(n_windows):
        chunk = Chunk(start = i * chunk_size, end = min((i + 1) * chunk_size, duration))
        for idx, word in enumerate(words[words_idx_start:]):
            if word.end <= chunk.end + eps or i == n_windows - 1:
                # chunk.words[idx + words_idx_start] = word.word
                chunk.words.append(word)
            else:
                break
        words_idx_start += len(chunk.words)
        chunks.append(chunk)
    return chunks


def render_transcription_chunk_word_indices(chunks: list[Chunk]) -> str:
    word_indices = ""
    idx_start = 0
    for chunk_idx, chunk in enumerate(chunks):
        word_indices += f"* W{chunk_idx}. " + str(
            {(i + idx_start): w.word for i, w in enumerate(chunk.words)}
        ) + "\n"
        idx_start += len(chunk.words)
    return word_indices


# from sudachipy import (
#     tokenizer as sudachi_tokenizer, 
#     dictionary as sudachi_dictionary
#     )
# _sudachi_tokenizer = None

# def _get_sudachi():
#     global _sudachi_tokenizer
#     if _sudachi_tokenizer is None:
#         _sudachi_tokenizer = sudachi_dictionary.Dictionary().create()
#     return _sudachi_tokenizer

FULLWIDTH_ALNUM_SPACE_MAP = str.maketrans({
    **{chr(ord("Ａ") + i): chr(ord("A") + i) for i in range(26)},
    **{chr(ord("ａ") + i): chr(ord("a") + i) for i in range(26)},
    **{chr(ord("０") + i): chr(ord("0") + i) for i in range(10)},
    "　": " ",
})

OPENING_PUNCTUATION = set("([{<《〈「『【〔（［｛“‘")
CLOSING_PUNCTUATION = set(")]}>》〉」』】〕）］｝”’")

_STANZA_PIPELINES: dict[str, object] = {}


def normalize_generated_text(text: str, language: str = "") -> str:
    """Normalize newly generated text at ASR/translation/reconstruction boundaries.

    Policy is intentionally narrow: Unicode NFC plus explicit full-width Latin
    letters, digits, and ideographic space conversion. Japanese kana/katakana are
    not converted to half-width here.
    """
    normalized = unicodedata.normalize("NFC", text or "")
    return normalized.translate(FULLWIDTH_ALNUM_SPACE_MAP)


def _get_jieba():
    import jieba
    return jieba


def _get_nagisa():
    import nagisa
    return nagisa


def _get_stanza_pipeline(language: str):
    lang = language.lower()
    if lang not in _STANZA_PIPELINES:
        import stanza
        _STANZA_PIPELINES[lang] = stanza.Pipeline(
            lang=lang,
            processors="tokenize",
            tokenize_no_ssplit=True,
            verbose=False,
        )
    return _STANZA_PIPELINES[lang]


def _tokenize_stanza(language: str, raw_text: str) -> list[str]:
    nlp = _get_stanza_pipeline(language)
    doc = nlp(raw_text)
    return [token.text for sentence in doc.sentences for token in sentence.tokens]


def _tokenize_regex(raw_text: str) -> list[str]:
    return re.findall(r"[^\s]+", raw_text)


def _configured_tokenizer(language: str) -> str:
    return Config.tokenizers.get(language.upper(), "stanza").lower()


def _is_align_char(ch: str, policy: str = "whisper") -> bool:
    cat = unicodedata.category(ch)

    if policy == "qwen":
        if ch == "'":
            return True
        return cat.startswith("L") or cat.startswith("N")

    if policy == "whisper":
        if ch == "'":
            return True
        return cat.startswith("L") or cat.startswith("N") or cat.startswith("M")

    raise ValueError(f"Unknown align char policy: {policy}")

def _align_text(
        text: str, 
        use_nfkc: bool = False,
        policy: str = "whisper"
    ) -> str:
    chars = []
    for ch in text:
        src = unicodedata.normalize("NFKC", ch) if use_nfkc else ch
        for c in src:
            if _is_align_char(c, policy):
                chars.append(c)
    return "".join(chars)

def _normalize_for_alignment(
        text: str, 
        use_nfkc: bool = False,
        policy: str = "whisper"
    ) -> tuple[str, list[int]]:
    normalized_chars = []
    orig_index_map = []

    for i, ch in enumerate(text):
        src = unicodedata.normalize("NFKC", ch) if use_nfkc else ch
        for c in src:
            if _is_align_char(c, policy):
                normalized_chars.append(c)
                orig_index_map.append(i)

    return "".join(normalized_chars), orig_index_map


def _normalized_spans_for_alignment(
        texts: list[str],
        use_nfkc: bool = False,
        policy: str = "whisper",
    ) -> list[tuple[int, int] | None]:
    """Return normalized half-open spans for each token/word surface.

    Each span is expressed in the concatenated alignment-normalized character
    space. Items that contribute no alignable characters receive ``None``.
    """
    spans: list[tuple[int, int] | None] = []
    cursor = 0
    for text in texts:
        normalized, _ = _normalize_for_alignment(text, use_nfkc, policy)
        if not normalized:
            spans.append(None)
            continue
        start = cursor
        end = cursor + len(normalized)
        spans.append((start, end))
        cursor = end
    return spans


def _has_align_char(text: str, policy: str = "whisper") -> bool:
    return any(_is_align_char(ch, policy) for ch in text)

def merge_symbol_punct_to_left(tokens: list[str], policy: str = "whisper") -> list[str]:
    if not tokens:
        return []

    merged = []
    for tok in tokens:
        if _has_align_char(tok, policy):
            merged.append(tok)
        else:
            if merged:
                merged[-1] += tok
            else:
                merged.append(tok)

    return merged


def merge_symbol_punct_to_neighbors(
    tokens: list[str],
    use_nfkc: bool = False,
    policy: str = "whisper",
) -> list[str]:
    """Attach punctuation/symbol-only tokens to neighboring lexical tokens.

    `merge_symbol_punct_to_left(...)` already covers punctuation that appears
    after an alignable token. This helper additionally handles leading
    punctuation by carrying it forward to the next alignable token. This keeps
    punctuation attached to words/characters instead of letting punctuation-only
    tokens enter alignment normalization.
    """

    if not tokens:
        return []

    merged: list[str] = []
    leading_punct = ""
    for tok in tokens:
        norm_tok, _ = _normalize_for_alignment(tok, use_nfkc, policy)
        if norm_tok:
            merged.append(leading_punct + tok)
            leading_punct = ""
            continue

        if merged:
            merged[-1] += tok
        else:
            leading_punct += tok

    if leading_punct:
        if merged:
            merged[-1] += leading_punct
        else:
            merged.append(leading_punct)

    return merged


def _is_opening_punctuation_token(token: str) -> bool:
    return bool(token) and all(ch in OPENING_PUNCTUATION for ch in token)


def _is_closing_punctuation_token(token: str) -> bool:
    return bool(token) and all(ch in CLOSING_PUNCTUATION for ch in token)


def attach_punctuation_to_surrounded_words(
    tokens: list[str],
    use_nfkc: bool = False,
    policy: str = "whisper",
) -> list[str]:
    """Attach punctuation-only tokens to surrounding lexical tokens.

    Opening punctuation attaches to the next lexical token; closing punctuation
    attaches to the previous lexical token. This keeps inner lexical tokens
    separate, e.g. ["《", "三国", "演义", "》"] becomes
    ["《三国", "演义》"].
    """
    if not tokens:
        return []

    merged: list[str] = []
    pending_prefix = ""
    for token in tokens:
        norm_token, _ = _normalize_for_alignment(token, use_nfkc, policy)
        if norm_token:
            merged.append(pending_prefix + token)
            pending_prefix = ""
            continue

        if _is_opening_punctuation_token(token):
            pending_prefix += token
        elif _is_closing_punctuation_token(token) and merged:
            merged[-1] += token
        elif merged:
            merged[-1] += token
        else:
            pending_prefix += token

    if pending_prefix:
        if merged:
            merged[-1] += pending_prefix
        else:
            merged.append(pending_prefix)
    return merged

# def _get_mapping_groups(
#         tokens: list[str], 
#         alignments: list[Word],
#         use_nfkc: bool = False,
#     ) -> list[list[int]]:
#     """
#     Construct word-level (we call token here) index groups from WisperX character-level alignment

#         Parameters:
#             - `tokens`: tokens from tokenizer like jieba, sudachi, ...
#             - `alignments`: forced aligment result from WisperX

#         Returns:
#             - A 2d grouping array, like [[0, 1], [2], [3, 4, 5]]
#     """
#     groups = []
#     char_ptr = 0
#     total_alignments = len(alignments)
    
#     for token_idx, token in enumerate(tokens):
#         token_len = len(_align_text(token, use_nfkc))
#         if token_len == 0:
#             continue
            
#         consumed_chars = 0
#         current_group = []
        
#         while consumed_chars < token_len and char_ptr < total_alignments:
#             curr_word = alignments[char_ptr]
#             curr_len = len(_align_text(curr_word.word, use_nfkc))
            
#             # if not curr_word.word.strip() and len(curr_word.word) == 0:
#             #     char_ptr += 1
#             #     continue

#             # curr_len = len(_align_text(curr_word.word, use_nfkc))
#             if curr_len == 0:
#                 char_ptr += 1
#                 continue
                
#             current_group.append(char_ptr)
#             consumed_chars += curr_len
#             char_ptr += 1
            
#         if consumed_chars != token_len:
#             token_key = _align_text(token, use_nfkc)
#             raise ValueError(
#                 "Mapping failed in _get_mapping_groups.\n"
#                 f"arguments:\n"
#                 f"  - tokens: {tokens}\n"
#                 f"  - aligments: {alignments}\n"
#                 f"  - use_nfkc: {use_nfkc}\n"
#                 f"token_idx={token_idx}, token={token!r}, token_key={token_key!r}, token_len={token_len}\n"
#                 f"consumed_chars={consumed_chars}, current_group={current_group}"
#             )

#         # if current_group:
#         groups.append(current_group)
            
#     return groups


def _get_mapping_groups(
        tokens: list[str],
        alignments: list[Word],
        use_nfkc: bool = False,
        policy: str = "whisper"
    ) -> list[list[int]]:
    """
    Construct word-level (we call token here) index groups from WisperX character-level alignment

        Parameters:
            - `tokens`: tokens from tokenizer like jieba, sudachi, ...
            - `alignments`: forced aligment result from WisperX

        Returns:
            - A 2d grouping array, like [[0, 1], [2], [3, 4, 5]]
    """

    token_keys = [_align_text(token, use_nfkc, policy) for token in tokens]
    align_keys = [_align_text(word.word, use_nfkc, policy) for word in alignments]

    groups: list[list[int]] = []
    token_ptr = 0
    align_ptr = 0
    total_tokens = len(tokens)
    total_alignments = len(alignments)

    while True:
        while token_ptr < total_tokens and not token_keys[token_ptr]:
            token_ptr += 1
        while align_ptr < total_alignments and not align_keys[align_ptr]:
            align_ptr += 1

        if token_ptr >= total_tokens:
            break

        start_token_ptr = token_ptr
        token_acc = ""
        align_acc = ""
        current_group: list[int] = []

        while True:
            token_is_prefix = (not token_acc) or align_acc.startswith(token_acc)
            align_is_prefix = (not align_acc) or token_acc.startswith(align_acc)

            if token_is_prefix and token_ptr < total_tokens:
                while token_ptr < total_tokens and not token_keys[token_ptr]:
                    token_ptr += 1
                if token_ptr < total_tokens:
                    token_acc += token_keys[token_ptr]
                    token_ptr += 1

            if align_is_prefix and align_ptr < total_alignments:
                while align_ptr < total_alignments and not align_keys[align_ptr]:
                    align_ptr += 1
                if align_ptr < total_alignments:
                    align_acc += align_keys[align_ptr]
                    current_group.append(align_ptr)
                    align_ptr += 1

            if token_acc == align_acc and token_acc:
                groups.append(current_group)
                break

            token_is_prefix = align_acc.startswith(token_acc)
            align_is_prefix = token_acc.startswith(align_acc)

            if not token_is_prefix and not align_is_prefix:
                raise ValueError(
                    "Mapping failed in _get_mapping_groups.\n"
                    f"arguments:\n"
                    f"  - tokens: {tokens}\n"
                    f"  - aligments: {alignments}\n"
                    f"  - use_nfkc: {use_nfkc}\n"
                    f"tokens[{start_token_ptr}:{token_ptr}]={tokens[start_token_ptr:token_ptr]!r}\n"
                    f"token_acc={token_acc!r}\n"
                    f"current_group={current_group}\n"
                    f"align_acc={align_acc!r}\n"
                    f"use_nfkc={use_nfkc}"
                )

            if token_ptr >= total_tokens and align_ptr >= total_alignments and token_acc != align_acc:
                raise ValueError(
                    "Mapping failed at end of stream in _get_mapping_groups.\n"
                    f"arguments:\n"
                    f"  - tokens: {tokens}\n"
                    f"  - aligments: {alignments}\n"
                    f"  - use_nfkc: {use_nfkc}\n"
                    f"tokens[{start_token_ptr}:{token_ptr}]={tokens[start_token_ptr:token_ptr]!r}\n"
                    f"token_acc={token_acc!r}\n"
                    f"current_group={current_group}\n"
                    f"align_acc={align_acc!r}\n"
                    f"use_nfkc={use_nfkc}"
                )

    while align_ptr < total_alignments and not align_keys[align_ptr]:
        align_ptr += 1

    if align_ptr != total_alignments:
        raise ValueError(
            "Unused alignment items remain after _get_mapping_groups.\n"
            f"align_ptr={align_ptr}, total_alignments={total_alignments}"
        )

    return groups


def reattach_punctuation_to_left(
    raw_text: str,
    clean_tokens: list[str],
    use_nfkc: bool = False,
    policy: str = "whisper"
    ) -> list[str]:
    """
    Reattach punctuation from raw_text back onto clean_tokens.

    Rule:
        Any punctuation between token_i and token_{i+1} is attached to token_i.
        Trailing punctuation after the last token is attached to the last token.
        Leading punctuation before the first token can optionally be attached to the first token.

    Args:
        raw_text:
            Original sentence/text with punctuation.
        clean_tokens:
            Token list from forced aligner, usually without punctuation.
        use_nfkc:
            Recover the clean tokens when tokenator used nfkc normalization

    Returns:
        Rebuilt token list with the same length as clean_tokens.
    """

    if not clean_tokens:
        return []

    clean_tokens = merge_symbol_punct_to_neighbors(clean_tokens, use_nfkc, policy)

    orig_norm, orig_map = _normalize_for_alignment(raw_text, use_nfkc, policy)

    if not orig_norm:
        rebuilt = "".join(ch for ch in raw_text if not ch.isspace())
        return [rebuilt] if rebuilt else []

    token_norms: list[str] = []
    for idx, tok in enumerate(clean_tokens):
        norm_tok, _ = _normalize_for_alignment(tok, use_nfkc, policy)
        if not norm_tok:
            raise ValueError(
                f"Token at index {idx} becomes empty after normalization: {tok!r}"
                f"  - raw_text: {raw_text}\n"
                f"  - clean_tokens: {clean_tokens}"
                )
        token_norms.append(norm_tok)

    joined_tokens_norm = "".join(token_norms)

    if joined_tokens_norm != orig_norm:
        # Report first mismatch position for debugging
        mismatch_pos = None
        min_len = min(len(joined_tokens_norm), len(orig_norm))
        for i in range(min_len):
            if joined_tokens_norm[i] != orig_norm[i]:
                mismatch_pos = i
                break
        if mismatch_pos is None and len(joined_tokens_norm) != len(orig_norm):
            mismatch_pos = min_len

        left = max(0, (mismatch_pos or 0) - 30)
        right = (mismatch_pos or 0) + 30

        raise ValueError(
            "Alignment failed.\n"
            f"Mismatch position: {mismatch_pos}\n"
            f"Tokens normalized snippet : {joined_tokens_norm[left:right]!r}\n"
            f"Original normalized snippet: {orig_norm[left:right]!r}"
        )

    # Convert normalized token boundaries back to original string spans
    spans: list[tuple[int, int]] = []
    cursor = 0
    for norm_tok in token_norms:
        start_norm = cursor
        end_norm = cursor + len(norm_tok) - 1
        start_orig = orig_map[start_norm]
        end_orig = orig_map[end_norm]
        spans.append((start_orig, end_orig))
        cursor = end_norm + 1

    rebuilt_tokens: list[str] = []

    for i, (start, end) in enumerate(spans):
        token_surface = raw_text[start : end + 1]
        next_start = spans[i + 1][0] if i + 1 < len(spans) else len(raw_text)
        gap = raw_text[end + 1 : next_start]
        gap = "".join(ch for ch in gap if not ch.isspace())
        rebuilt_tokens.append(token_surface + gap)

    leading = raw_text[: spans[0][0]]
    leading = "".join(ch for ch in leading if not ch.isspace())
    if leading:
        rebuilt_tokens[0] = leading + rebuilt_tokens[0]

    return rebuilt_tokens


def restore_alignment_token_surfaces(
    raw_text: str,
    clean_tokens: list[str],
    use_nfkc: bool = False,
    policy: str = "whisper",
) -> list[str]:
    """Restore final project-facing alignment token surfaces.

    This is the shared wrapper-facing restoration entry point. It keeps the
    existing span-matching behavior, then applies pair-aware punctuation
    attachment for punctuation-only tokens.
    """
    restored = reattach_punctuation_to_left(raw_text, clean_tokens, use_nfkc, policy)
    return attach_punctuation_to_surrounded_words(restored, use_nfkc, policy)

def apply_mapping_groups(
        alignments: list[Word], 
        word_mapping_groups: list[list[int]],
        language: Optional[str] = None,
    ) -> list[Word]:
    """
    Convert grouping array into word-level alignment

        Parameters:
            - `alignments`: forced aligment result from WisperX
            - `groups`: A 2d grouping array, like [[0, 1], [2], [3, 4, 5]]

        Returns:
            - A word-level alignment
    """
    if len(word_mapping_groups) == len(alignments):
        return alignments

    merged_words = []
    separator = ""
    if language is not None and language.lower() not in ("zh", "ja"):
        separator = " "
    
    for group in word_mapping_groups:
        if not group:
            continue
            
        merged_text = separator.join([alignments[i].word for i in group])
        
        start_time = alignments[group[0]].start
        end_time = alignments[group[-1]].end
        
        merged_words.append(Word(word=merged_text, start=start_time, end=end_time))
        
    return merged_words


def _process_chinese_words(whisperx_char_alignments: list[Word]) -> list[list[int]]:
    if not whisperx_char_alignments:
        return []
        
    raw_text = "".join([w.word for w in whisperx_char_alignments])
    
    tokens = tokenize(language="ZH", raw_text=raw_text, indexing=False)
    groups = _get_mapping_groups(tokens, whisperx_char_alignments)
    # return apply_mapping_groups(groups, whisperx_char_alignments)
    return groups


def _process_japanese_words(whisperx_char_alignments: list[Word]) -> list[list[int]]:
    if not whisperx_char_alignments:
        return []
    
    raw_text = "".join([w.word for w in whisperx_char_alignments])
    
    tokens = tokenize(language="JA", raw_text=raw_text, indexing=False)
    groups = _get_mapping_groups(tokens, whisperx_char_alignments, use_nfkc = True)
    # return apply_mapping_groups(groups, whisperx_char_alignments)
    return groups

def _restore_korean_eojeols(raw_text: str, whisperx_char_alignments: list[Word]) -> list[list[int]]:
    correct_eojeols = raw_text.split(" ")
    
    groups = []
    char_ptr = 0 
    total_alignments = len(whisperx_char_alignments)
    
    for eojeol in correct_eojeols:
        if not eojeol.strip():
            continue
            
        chars_to_consume = len(eojeol)
        consumed = 0
        current_group = []
        
        while consumed < chars_to_consume and char_ptr < total_alignments:
            current_char_obj = whisperx_char_alignments[char_ptr]
            
            if not current_char_obj.word.strip() and len(current_char_obj.word) == 0:
                char_ptr += 1
                continue
                
            current_group.append(char_ptr)
            
            consumed += len(current_char_obj.word)
            char_ptr += 1
            
        if current_group:
            groups.append(current_group)
            
    return groups


def process_words(
        language: str, 
        whisperx_char_alignments: list[Word], 
        raw_text: Optional[str] = None
    ) -> list[list[int]]:
    """
    Recunstruct 2d grouping array for ZH (Chinese), JA (Japanese), KO (Korean) from whisperx char alignments. Other languages will return the raw alignment.

        Returns:
            - A 2d grouping array, like [[0, 1], [2], [3, 4, 5]]
    """
    if language.lower() == "zh":
        groups = _process_chinese_words(whisperx_char_alignments)
    elif language.lower() == "ja":
        groups = _process_japanese_words(whisperx_char_alignments)
    elif language.lower() == "ko":
        if raw_text is None:
            raise Exception(f"`raw_text` is needed for Korean")
        groups = _restore_korean_eojeols(raw_text, whisperx_char_alignments)
    else:
        groups = [[i] for i, _ in enumerate(whisperx_char_alignments)]

    return groups

def tokenize(
        language: str,
        raw_text: str,
        indexing: bool = True,
    ) -> dict | list:
    lang = language.upper()
    backend = _configured_tokenizer(lang)

    if backend == "stanza":
        raw_tokens = _tokenize_stanza(lang.lower(), raw_text)
        raw_tokens = attach_punctuation_to_surrounded_words(raw_tokens, use_nfkc=(lang == "JA"))
    elif lang == "ZH" and backend == "jieba":
        raw_tokens = list(_get_jieba().cut(raw_text))
        raw_tokens = attach_punctuation_to_surrounded_words(raw_tokens)
    elif lang == "JA" and backend == "nagisa":
        # sudachi = _get_sudachi()
        # raw_tokens = [m.surface() for m in sudachi.tokenize(raw_text, sudachi_tokenizer.Tokenizer.SplitMode.C)]
        nagisa_tokens = [token for token in _get_nagisa().tagging(raw_text).words]
        nagisa_tokens = attach_punctuation_to_surrounded_words(nagisa_tokens, use_nfkc=True)
        raw_tokens = restore_alignment_token_surfaces(raw_text, nagisa_tokens, use_nfkc=True)
    elif backend in ("regex", "whitespace"):
        raw_tokens = _tokenize_regex(raw_text) if backend == "regex" else raw_text.split()
    else:
        raise ValueError(f"Unsupported tokenizer backend for {lang}: {backend}")

    tokens = [token.strip() for token in raw_tokens if token.strip()]
    
    if indexing:
        return {i: token for i, token in enumerate(tokens)}
    else:
        return tokens


def align_text_tokens_to_words(
        language: str,
        tokens: list[str],
        words: list[Word],
    ) -> list[list[int]]:
    """
    Align explicit text tokens to reconstructed source word indices.

    This keeps downstream source-token consumers in the same token index space as
    target-centric mapping prompts while still projecting those tokens onto timed
    source words.
    """
    use_nfkc = language.lower() == "ja"
    token_spans = _normalized_spans_for_alignment(tokens, use_nfkc=use_nfkc)
    word_spans = _normalized_spans_for_alignment([word.word for word in words], use_nfkc=use_nfkc)

    token_groups: list[list[int]] = []
    word_ptr = 0
    total_words = len(words)

    for token_idx, token_span in enumerate(token_spans):
        if token_span is None:
            token_groups.append([])
            continue

        token_start, token_end = token_span

        while word_ptr < total_words:
            word_span = word_spans[word_ptr]
            if word_span is None or word_span[1] <= token_start:
                word_ptr += 1
                continue
            break

        scan_ptr = word_ptr
        current_group: list[int] = []
        while scan_ptr < total_words:
            word_span = word_spans[scan_ptr]
            if word_span is None:
                scan_ptr += 1
                continue

            word_start, word_end = word_span
            if word_start >= token_end:
                break
            if word_end > token_start and word_start < token_end:
                current_group.append(scan_ptr)
            scan_ptr += 1

        if not current_group:
            raise ValueError(
                "Token-to-word projection failed in align_text_tokens_to_words.\n"
                f"language={language!r}\n"
                f"token_idx={token_idx}\n"
                f"token={tokens[token_idx]!r}\n"
                f"normalized_token_span={(token_start, token_end)}\n"
                f"words={[word.word for word in words]!r}"
            )

        token_groups.append(current_group)

    return token_groups


def group_tokens_by_sense_units(
        language: str,
        tokens: list[str],
        sense_unit_groups: list[list[int]],
    ) -> dict[int, str]:
    grouped_texts: dict[int, str] = {}
    for sense_unit_index, group in enumerate(sense_unit_groups):
        grouped_texts[sense_unit_index] = sense_unit_indices_to_text(
            language=language,
            tokens=tokens,
            indices=group,
        )
    return grouped_texts


def sense_unit_indices_to_text(
        language: str,
        tokens: list[str],
        indices: list[int],
    ) -> str:
    grouped_tokens = [tokens[idx] for idx in indices if 0 <= idx < len(tokens)]
    if language.lower() in ("zh", "ja"):
        return "".join(grouped_tokens)
    return " ".join(grouped_tokens)
