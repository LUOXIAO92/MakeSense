from .schema import Word, SenseUnits, MetaData, Transcription, Translation
from .utils import (
    build_transcription_chunks,
    apply_mapping_groups,
    sense_unit_indices_to_text,
)

def build_asr_blocks(
    metadata: MetaData,
    transcription: Transcription,
    eps: float = 1e-6,
    debug: bool = False
) -> list[str]:
    """
    Return
        asr_blocks: Each element represents a configured audio chunk.
            - `["<src><sense unit 1></src>","<src><sense unit 2></src>","<src><|wait|></src>", ..., "<src><sense unit N></src>"]`

        debug: Only for debugging
            - True: `<src start={start_time}><sense unit></src end={start_time}>`
            - False: `<src><sense unit></src>`
    """

    duration = metadata.duration
    tokens   = transcription.tokens
    words    = apply_mapping_groups(tokens, transcription.words, language=transcription.language)
    chunks   = build_transcription_chunks(duration = duration, words = words)
    groups   = transcription.sense_units.groups

    groups_word_list = []
    for group_idices in groups:
        group = ""
        for idx in group_idices:
            if transcription.language.lower() in ("zh", "ja"):
                group += words[idx].word
            else:
                group += (words[idx].word + " ")
        groups_word_list.append(group)

    asr_blocks = []
    group_idx = 0
    for chunk in chunks:
        words_inside_one_chunk = ""
        start = chunk.start
        end = chunk.end
        for group in groups[group_idx:]:
            seg_end = words[group[-1]].end
            
            if seg_end < end + eps:
                words_inside_one_chunk += groups_word_list[group_idx]
                group_idx += 1
            else :
                break

        start_ele = f"start={start:.2f}" if debug else ""
        end_ele   = f"end={end:.2f}" if debug else ""
        timestamp = "; " + start_ele + ", " + end_ele if debug else ""
        if words_inside_one_chunk:
            asr_blocks.append(f"<src>{words_inside_one_chunk}</src>{timestamp}")
        else:
            asr_blocks.append(f"<src><|wait|></src>{timestamp}")

    return asr_blocks


def build_translation_blocks(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    tolerance_window: int = 0,
    eps: float = 1e-6,
    debug: bool = False,
) -> tuple[list[str], int]:
    """
    Return
        translation_blocks: Each element represents a config-defined audio chunk.
            - ["<tgt><sense unit 1></tgt>", "<tgt><|wait|></tgt>", ..., "<tgt><sense unit N></tgt>"]

        max_empty_window_count:
            The maximum number of consecutive final output windows that contain
            `<tgt><|wait|></tgt>`. This is computed from the actual emitted block
            sequence, not inferred from `tolerance_window`.

        tolerance_window:
            Non-negative target emission cadence.
            - 0 means emit target sense units at the first window where their mapped source tokens
              are available under the source sense-unit release frontier.
            - N > 0 means target emission is allowed only at window N, then every N + 1 windows.
            At each allowed window, all consecutive target sense units already supported by source
            evidence are emitted together. Target sense units are never emitted before their mapped
            source-token evidence is available under the source sense-unit release frontier, and
            trailing ready units are not force-flushed if no later cadence window exists.

        debug: Only for debugging. Appends the same window timestamp suffix as `build_asr_blocks(...)`.
    """
    if tolerance_window < 0:
        raise ValueError("tolerance_window must be non-negative")

    duration = metadata.duration
    tokens = transcription.tokens
    words = apply_mapping_groups(tokens, transcription.words, language=transcription.language)
    if not words:
        raise ValueError("Cannot build translation blocks without reconstructed source words")

    chunks = build_transcription_chunks(duration=duration, words=words)
    if not chunks:
        raise ValueError("Cannot build translation blocks without source windows")

    source_groups = transcription.sense_units.groups
    word_release_window_indices: list[int | None] = [None] * len(words)
    group_idx = 0
    for chunk_idx, chunk in enumerate(chunks):
        is_final_chunk = chunk_idx == len(chunks) - 1
        while group_idx < len(source_groups):
            group = source_groups[group_idx]
            if not group:
                raise ValueError(f"Empty source sense unit group at index {group_idx}")
            last_word_idx = group[-1]
            if last_word_idx < 0 or last_word_idx >= len(words):
                raise ValueError(
                    f"source sense unit group {group_idx} contains word index out of range: "
                    f"{last_word_idx}; available source words: {len(words)}"
                )
            seg_end = words[last_word_idx].end
            last_word_is_in_chunk = any(word is words[last_word_idx] for word in chunk.words)
            last_token_final_overrun = is_final_chunk and last_word_idx == len(words) - 1 and last_word_is_in_chunk
            if seg_end < chunk.end + eps or last_token_final_overrun:
                for word_id in group:
                    if word_id < 0 or word_id >= len(words):
                        raise ValueError(
                            f"source sense unit group {group_idx} contains word index out of range: "
                            f"{word_id}; available source words: {len(words)}"
                        )
                    word_release_window_indices[word_id] = chunk_idx
                group_idx += 1
            else:
                break

    if group_idx < len(source_groups):
        raise ValueError(
            "Not all source sense units were assigned to a release window: "
            f"assigned={group_idx}, total={len(source_groups)}"
        )
    for word_id, release_window in enumerate(word_release_window_indices):
        if release_window is None:
            raise ValueError(f"source word {word_id} was not covered by any source sense unit group")

    source_token_ready_windows: list[int] = []
    for word_id, release_window_idx in enumerate(word_release_window_indices):
        if release_window_idx is None:
            raise ValueError(f"source word {word_id} has no release window")
        source_token_ready_windows.append(release_window_idx)

    target_groups = translation.sense_units.groups
    target_tokens = list(translation.tokens)
    if not target_tokens:
        raise ValueError(
            "Cannot build translation blocks without canonical target tokens. "
            "translation.tokens must be populated by pure-text segmentation before mapping/dataset projection."
        )

    target_text_by_id: dict[int, str] = {}
    target_ready_window_by_id: dict[int, int] = {}

    for mapping in translation.mappings:
        target_senseunit_id = mapping.target_senseunit_id
        if target_senseunit_id < 0 or target_senseunit_id >= len(target_groups):
            raise ValueError(
                f"target_senseunit_id out of range: {target_senseunit_id}; "
                f"available target sense units: {len(target_groups)}"
            )

        source_token_ids = mapping.source_token_ids
        if not source_token_ids:
            raise ValueError(
                f"source_token_ids must be non-empty for target_senseunit_id={target_senseunit_id}"
            )

        ready_window_idx = 0
        for source_token_id in source_token_ids:
            if source_token_id < 0 or source_token_id >= len(source_token_ready_windows):
                raise ValueError(
                    f"source_token_id/source word id out of range: {source_token_id}; "
                    f"available source words: {len(source_token_ready_windows)}"
                )
            ready_window_idx = max(ready_window_idx, source_token_ready_windows[source_token_id])

        target_text = sense_unit_indices_to_text(
            language=translation.language,
            tokens=target_tokens,
            indices=target_groups[target_senseunit_id],
        )
        target_text_by_id[target_senseunit_id] = target_text
        target_ready_window_by_id[target_senseunit_id] = ready_window_idx

    emissions_by_window: dict[int, list[str]] = {}
    next_target_senseunit_id = 0
    if tolerance_window == 0:
        allowed_emit_window_indices = range(len(chunks))
    else:
        allowed_emit_window_indices = range(tolerance_window, len(chunks), tolerance_window + 1)

    for emit_window_idx in allowed_emit_window_indices:
        while next_target_senseunit_id in target_ready_window_by_id:
            if target_ready_window_by_id[next_target_senseunit_id] > emit_window_idx:
                break
            emissions_by_window.setdefault(emit_window_idx, []).append(target_text_by_id[next_target_senseunit_id])
            next_target_senseunit_id += 1

    translation_blocks = []
    max_empty_window_count = 0
    current_empty_window_count = 0
    for chunk_idx, chunk in enumerate(chunks):
        start_ele = f"start={chunk.start:.2f}" if debug else ""
        end_ele = f"end={chunk.end:.2f}" if debug else ""
        timestamp = "; " + start_ele + ", " + end_ele if debug else ""

        emissions = emissions_by_window.get(chunk_idx, [])
        if emissions:
            max_empty_window_count = max(max_empty_window_count, current_empty_window_count)
            current_empty_window_count = 0
            target_text = "".join(emissions) if translation.language.lower() in ("zh", "ja") else " ".join(emissions)
            translation_blocks.append(f"<tgt>{target_text}</tgt>{timestamp}")
        else:
            current_empty_window_count += 1
            translation_blocks.append(f"<tgt><|wait|></tgt>{timestamp}")

    max_empty_window_count = max(max_empty_window_count, current_empty_window_count)

    return translation_blocks, max_empty_window_count
