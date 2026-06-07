from .schema import Word, SenseUnits, MetaData, Transcription, Translation
from .utils import (
    build_transcription_chunks,
    apply_mapping_groups,
    sense_unit_indices_to_text,
)


def _assign_source_sense_units_to_release_windows(
    *,
    chunks,
    words: list[Word],
    source_groups: list[list[int]],
    eps: float,
) -> tuple[list[int | None], list[int | None], int]:
    word_release_window_indices: list[int | None] = [None] * len(words)
    group_release_window_indices: list[int | None] = [None] * len(source_groups)
    group_idx = 0
    for chunk_idx, chunk in enumerate(chunks):
        is_final_chunk = chunk_idx == len(chunks) - 1
        chunk_word_ids = {
            word_id
            for word_id, word in enumerate(words)
            if any(chunk_word is word for chunk_word in chunk.words)
        }
        tail_absorption_active = False
        while group_idx < len(source_groups):
            group = source_groups[group_idx]
            if not group:
                raise ValueError(f"Empty source sense unit group at index {group_idx}")
            for word_id in group:
                if word_id < 0 or word_id >= len(words):
                    raise ValueError(
                        f"source sense unit group {group_idx} contains word index out of range: "
                        f"{word_id}; available source words: {len(words)}"
                    )

            first_word_idx = group[0]
            last_word_idx = group[-1]
            seg_end = words[last_word_idx].end
            group_reaches_final_chunk = any(word_id in chunk_word_ids for word_id in group)
            group_overlaps_final_window = words[first_word_idx].start < chunk.end + eps
            final_chunk_absorbed_group = (
                is_final_chunk
                and group_reaches_final_chunk
                and (tail_absorption_active or group_overlaps_final_window)
            )
            if seg_end < chunk.end + eps or final_chunk_absorbed_group:
                for word_id in group:
                    word_release_window_indices[word_id] = chunk_idx
                group_release_window_indices[group_idx] = chunk_idx
                if final_chunk_absorbed_group and seg_end >= chunk.end + eps:
                    tail_absorption_active = True
                group_idx += 1
            else:
                break

    return group_release_window_indices, word_release_window_indices, group_idx


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
    groups   = [list(group) for group in transcription.sense_units.groups]
    group_release_window_indices, _, _ = _assign_source_sense_units_to_release_windows(
        chunks=chunks,
        words=words,
        source_groups=groups,
        eps=eps,
    )

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
    for chunk_idx, chunk in enumerate(chunks):
        words_inside_one_chunk = ""
        start = chunk.start
        end = chunk.end
        while group_idx < len(groups):
            if group_release_window_indices[group_idx] == chunk_idx:
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


def count_max_empty_translation_windows(translation_blocks: list[str]) -> int:
    """Count the maximum consecutive target wait windows in rendered blocks."""

    max_empty_window_count = 0
    current_empty_window_count = 0
    for block in translation_blocks:
        if "<tgt><|wait|></tgt>" in block:
            current_empty_window_count += 1
        else:
            max_empty_window_count = max(max_empty_window_count, current_empty_window_count)
            current_empty_window_count = 0
    return max(max_empty_window_count, current_empty_window_count)


def _build_translation_blocks_with_allowed_windows(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    *,
    allowed_emit_window_indices,
    eps: float = 1e-6,
    debug: bool = False,
) -> list[str]:
    """
    Return
        translation_blocks: Each element represents a config-defined audio chunk.
            - ["<tgt><sense unit 1></tgt>", "<tgt><|wait|></tgt>", ..., "<tgt><sense unit N></tgt>"]

        debug: Only for debugging. Appends the same window timestamp suffix as `build_asr_blocks(...)`.
    """
    duration = metadata.duration
    tokens = transcription.tokens
    words = apply_mapping_groups(tokens, transcription.words, language=transcription.language)
    if not words:
        raise ValueError("Cannot build translation blocks without reconstructed source words")

    chunks = build_transcription_chunks(duration=duration, words=words)
    if not chunks:
        raise ValueError("Cannot build translation blocks without source windows")

    source_groups = transcription.sense_units.groups
    _, word_release_window_indices, group_idx = _assign_source_sense_units_to_release_windows(
        chunks=chunks,
        words=words,
        source_groups=[list(group) for group in source_groups],
        eps=eps,
    )

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
    for emit_window_idx in allowed_emit_window_indices:
        while next_target_senseunit_id in target_ready_window_by_id:
            if target_ready_window_by_id[next_target_senseunit_id] > emit_window_idx:
                break
            emissions_by_window.setdefault(emit_window_idx, []).append(target_text_by_id[next_target_senseunit_id])
            next_target_senseunit_id += 1

    translation_blocks = []
    for chunk_idx, chunk in enumerate(chunks):
        start_ele = f"start={chunk.start:.2f}" if debug else ""
        end_ele = f"end={chunk.end:.2f}" if debug else ""
        timestamp = "; " + start_ele + ", " + end_ele if debug else ""

        emissions = emissions_by_window.get(chunk_idx, [])
        if emissions:
            target_text = "".join(emissions) if translation.language.lower() in ("zh", "ja") else " ".join(emissions)
            translation_blocks.append(f"<tgt>{target_text}</tgt>{timestamp}")
        else:
            translation_blocks.append(f"<tgt><|wait|></tgt>{timestamp}")

    return translation_blocks


def _build_conservative_translation_blocks_with_min_wait(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    *,
    min_wait_window: int,
    eps: float = 1e-6,
    debug: bool = False,
) -> list[str]:
    """Build natural translation blocks throttled by a minimum wait-block gap.

    ``min_wait_window=N`` means each target release must be preceded by at
    least ``N`` consecutive target wait blocks. If natural translation has
    already waited long enough, the ready target text is released immediately;
    otherwise ready text is buffered until the gap is satisfied.
    """

    duration = metadata.duration
    tokens = transcription.tokens
    words = apply_mapping_groups(tokens, transcription.words, language=transcription.language)
    if not words:
        raise ValueError("Cannot build translation blocks without reconstructed source words")

    chunks = build_transcription_chunks(duration=duration, words=words)
    if not chunks:
        raise ValueError("Cannot build translation blocks without source windows")

    source_groups = transcription.sense_units.groups
    _, word_release_window_indices, group_idx = _assign_source_sense_units_to_release_windows(
        chunks=chunks,
        words=words,
        source_groups=[list(group) for group in source_groups],
        eps=eps,
    )

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
    pending_emissions: list[str] = []
    next_target_senseunit_id = 0
    last_emit_window_idx = -1
    for chunk_idx in range(len(chunks)):
        while next_target_senseunit_id in target_ready_window_by_id:
            if target_ready_window_by_id[next_target_senseunit_id] > chunk_idx:
                break
            pending_emissions.append(target_text_by_id[next_target_senseunit_id])
            next_target_senseunit_id += 1

        waited_windows = chunk_idx - last_emit_window_idx - 1
        if pending_emissions and waited_windows >= min_wait_window:
            emissions_by_window[chunk_idx] = pending_emissions
            pending_emissions = []
            last_emit_window_idx = chunk_idx

    translation_blocks = []
    for chunk_idx, chunk in enumerate(chunks):
        start_ele = f"start={chunk.start:.2f}" if debug else ""
        end_ele = f"end={chunk.end:.2f}" if debug else ""
        timestamp = "; " + start_ele + ", " + end_ele if debug else ""

        emissions = emissions_by_window.get(chunk_idx, [])
        if emissions:
            target_text = "".join(emissions) if translation.language.lower() in ("zh", "ja") else " ".join(emissions)
            translation_blocks.append(f"<tgt>{target_text}</tgt>{timestamp}")
        else:
            translation_blocks.append(f"<tgt><|wait|></tgt>{timestamp}")

    return translation_blocks


def build_translation_blocks(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    eps: float = 1e-6,
    debug: bool = False,
) -> list[str]:
    """Build natural translation blocks: emit once source evidence is ready."""

    duration = metadata.duration
    words = apply_mapping_groups(transcription.tokens, transcription.words, language=transcription.language)
    chunks = build_transcription_chunks(duration=duration, words=words)
    return _build_translation_blocks_with_allowed_windows(
        metadata,
        transcription,
        translation,
        allowed_emit_window_indices=range(len(chunks)),
        eps=eps,
        debug=debug,
    )


def build_fixed_window_translation_blocks(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    tolerance_window: int = 0,
    eps: float = 1e-6,
    debug: bool = False,
) -> list[str]:
    """Build fixed-cadence translation blocks.

    ``tolerance_window=0`` is equivalent to natural translation.  ``N > 0``
    permits target emission only at window ``N`` and then every ``N + 1`` windows.
    """

    if tolerance_window < 0:
        raise ValueError("tolerance_window must be non-negative")
    if tolerance_window == 0:
        return build_translation_blocks(metadata, transcription, translation, eps=eps, debug=debug)

    duration = metadata.duration
    words = apply_mapping_groups(transcription.tokens, transcription.words, language=transcription.language)
    chunks = build_transcription_chunks(duration=duration, words=words)
    return _build_translation_blocks_with_allowed_windows(
        metadata,
        transcription,
        translation,
        allowed_emit_window_indices=range(tolerance_window, len(chunks), tolerance_window + 1),
        eps=eps,
        debug=debug,
    )


def build_conservative_translation_blocks(
    metadata: MetaData,
    transcription: Transcription,
    translation: Translation,
    min_wait_window: int,
    eps: float = 1e-6,
    debug: bool = False,
) -> list[str]:
    """Build conservative natural translation blocks with a minimum wait-block gap."""

    if min_wait_window < 0:
        raise ValueError("min_wait_window must be non-negative")
    return _build_conservative_translation_blocks_with_min_wait(
        metadata,
        transcription,
        translation,
        min_wait_window=min_wait_window,
        eps=eps,
        debug=debug,
    )
