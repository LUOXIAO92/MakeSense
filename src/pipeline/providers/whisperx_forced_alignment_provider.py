import gc
import torch
import torchaudio
import unicodedata
import whisperx
from pathlib import Path
from dataclasses import dataclass
from typing import Literal

from configs.config import Config
from core.schema import Word
from core.utils import process_words, restore_alignment_token_surfaces

@dataclass
class StripState:
    removed: list[tuple[int, str]]

def _is_text_char(ch: str) -> bool:
    """
    "Text char" definition (character-level):
      - Letters: Unicode category L*
      - Marks (combining marks): M*
      - Numbers: N*
      - ASCII apostrophe (') for contractions / possessives
      - Optional: whitespace (isspace)
    Everything else (P* punctuation, S* symbols, C* control, etc.) is removed.
    """
    if ch.isspace():
        return True
    if ch == "'":
        return True
    return unicodedata.category(ch)[0] in ("L", "M", "N")

def _strip_non_text_symbols(text: str):
    kept = []
    removed = []
    for ch in text:
        if _is_text_char(ch):
            kept.append(ch)
        else:
            removed.append((len(kept), ch))
    cleaned = "".join(kept)
    return cleaned, StripState(removed = removed)

def _flatten_to_single_chars(words: list[Word]):
    flat: list[Word] = []
    for w in words:
        if len(w.word) == 1:
            flat.append(w)
        else:
            for ch in w.word:
                flat.append(Word(word=ch, start=w.start, end=w.end))
    return flat

def _ensure_has_spaces_like_cleaned(
    cleaned_text: str,
    flat_chars: list[Word],
    ):
    def _anchor_time(out: list[Word]) -> float:
        if out:
            return out[-1].end
        if flat_chars:
            return flat_chars[0].start
        return 0.0

    out: list[Word] = []
    j = 0  # index over flat_chars (non-space chars from aligner)
    for i, ch in enumerate(cleaned_text):
        if ch == " ":
            t = _anchor_time(out)
            out.append(Word(word=" ", start=t, end=t))
        else:
            if j >= len(flat_chars):
                t = _anchor_time(out)
                out.append(Word(word=ch, start=t, end=t))
            else:
                out.append(flat_chars[j])
                j += 1

    return out

def _reinsert_symbols_into_char_alignment(
    cleaned_words: list[Word],
    state:  StripState,
    anchor: Literal["prev_end", "next_start", "between"] = "between"
    ):
    """
    Takes character-level alignment for CLEANED text and reinserts removed symbols,
    attaching each symbol after the preceding character (pos-1).
    """

    n = len(cleaned_words)
    if n == 0:
        merged = "".join(ch for _, ch in state.removed)
        return [Word(word = merged, start = 0.0, end = 0.0)] if merged else []

    buckets: list[list[str]] = [[] for _ in range(n + 1)]
    for pos, sym in state.removed:
        if pos < 0:
            pos = 0
        elif pos > n:
            pos = n
        buckets[pos].append(sym)

    out: list[Word] = []

    def _anchor_time(pos):
        if anchor == "prev_end":
            return cleaned_words[0].start if pos == 0 else cleaned_words[pos - 1].end
        if anchor == "next_start":
            return cleaned_words[pos].start if pos < n else cleaned_words[n - 1].end
        if anchor == "between":
            if pos == 0:
                return cleaned_words[0].start
            if pos == n:
                return cleaned_words[n - 1].end
            return (cleaned_words[pos - 1].end + cleaned_words[pos].start) / 2.0
        raise ValueError("anchor must be one of: prev_end, next_start, between")

    for i in range(n):
        if buckets[i]:
            t = _anchor_time(i)
            for sym in buckets[i]:
                out.append(Word(word=sym, start=t, end=t))
        w = cleaned_words[i]
        out.append(Word(word=w.word, start=w.start, end=w.end))

    if buckets[n]:
        t = _anchor_time(n)
        for sym in buckets[n]:
            out.append(Word(word=sym, start=t, end=t))

    return out


def _merge_ascii_to_word(
    words: list[Word],
    ):

    out: list[Word] = []
    buf = []
    buf_start = 0.0
    buf_end   = 0.0

    def flush():
        nonlocal buf
        if buf:
            out.append(Word(word = "".join(buf), start = buf_start, end = buf_end))
            buf = []

    def is_ascii_alnum(ch: str):
        return (
            len(ch) == 1 and (ord(ch) < 128) and (not ch.isspace())
            # (("A" <= ch <= "Z") or ("a" <= ch <= "z") or ("0" <= ch <= "9"))
        )

    for w in words:
        ch = w.word

        if len(ch) != 1:
            flush()
            out.append(w)
            continue

        if is_ascii_alnum(ch):
            if not buf:
                buf_start = w.start
            buf.append(ch)
            buf_end = w.end
        else:
            flush()
            out.append(w)

    flush()
    return out



class WhisperXForcedAlignment:
    def __init__(
        self,
        model_name: str,
        language: str,
        device: str = "cpu",
        ):
        """
        Arguments
            - model_name:
                HuggingFace repo id or local directory.
            - language:
                Language name (e.g., "Chinese") or language code (e.g., "zh").
            - device:
                Device to run the model_name on (e.g., "cuda", "cpu", "mps").
        """
        self.model_name  = model_name
        self.device = device

        if language.capitalize() in Config.language_names:
            self.lang = Config.lang_name2code.get(language.capitalize()).lower()
        if language.upper() in Config.language_codes:
            self.lang = language.lower()
        else:
            self.lang = None 

        self.align_model = None
        self.model_metadata = None
        
    def load(self):
        self.align_model, self.model_metadata = whisperx.load_align_model(
            language_code = self.lang.lower(),
            model_name    = self.model_name,
            device        = self.device
            )
        return self
    
    def unload(self):
        if self.align_model is not None:
            self.align_model = None

        gc.collect()

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        return self
        
    def align(
            self,
            text: str,
            audio: str | Path,
            duration: float | None = None,
        ):
        cleaned_text, strip_state = _strip_non_text_symbols(text)

        waveform, sample_rate = torchaudio.load(audio)

        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(sample_rate, 16000)
            waveform = resampler(waveform)

        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim = 0, keepdim = True)
            
        _duration = duration if duration else waveform.shape[1] / sample_rate
        segments = [
            {
                "text": cleaned_text,
                "start": 0.0,
                "end": _duration 
            }
        ]

        result = whisperx.align(
            segments, 
            self.align_model, 
            self.model_metadata, 
            waveform, 
            self.align_model.device, 
            return_char_alignments = True
            )

        tokens: list[Word] = []
        for seg in result["segments"]:
            for word in seg["words"]:
                tokens.append(Word(word = word["word"], start = word["start"], end = word["end"]))
                
        tokens = _flatten_to_single_chars(tokens)
        tokens = _ensure_has_spaces_like_cleaned(cleaned_text, tokens)

        tokens = _reinsert_symbols_into_char_alignment(tokens, strip_state)
        tokens = _merge_ascii_to_word(tokens)
        tokens = [w for w in tokens if not (len(w.word) == 1 and w.word.isspace())]
        restored_surfaces = restore_alignment_token_surfaces(
            text,
            [w.word for w in tokens],
            policy="whisper",
        )
        tokens = [
            Word(word=surface, start=word.start, end=word.end)
            for word, surface in zip(tokens, restored_surfaces)
        ]
        words = process_words(self.lang.upper(), tokens, text)

        return tokens, words
