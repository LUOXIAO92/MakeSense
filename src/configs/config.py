"""
Configuration file.
**NOTE**: Do not instantiate the object, like config = Config(). Just asscess the members like asr_model = Config.asr_models.Chinese
"""
from enum import Enum
from typing import Literal


# --- Dataset configs: start ---
SEED              = 4021
N_SAMPLES         = 8000
RECORD_LIMIT      = 1000
MIN_DURATION_TIME = 10
MAX_DURATION_TIME = 60
# --- Dataset configs: end ---


# --- Language support block: start ---
"""
Add language support if you want, but ensure that you already have supported tokenizer, asr model, forced alignment model and language pack

## Forced alignment model support

Wav2vec2 forced alignment model is also supported. WhisperX package is needed. 
Please install it via `pip install whisperx`.

Example:

```python
FORCED_ALIGNMENT_MODELS = {
    "ZH": "jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn",
    "EN": "jonatasgrosman/wav2vec2-large-xlsr-53-english",
    "JA": "jonatasgrosman/wav2vec2-large-xlsr-53-japanese",
    "KO": "kresnik/wav2vec2-large-xlsr-korean"
    }
```

## Asr model support

Whisper is supported.

Example:

```python
ASR_MODELS = {
    "ZH": "...",
    "EN": "...",
    "JA": "...",
    "KO": "...",
    }
```

## Tokenizer support

`stanza` is reconmanded, which is the latest multilingual NLP project. Refer to https://stanfordnlp.github.io/stanza/ .
- For Chinese, you can use `jieba` as an alternative.
- For Japanese, you can use `nagisa`.
- English and Korean can be empty since they already included spaces.

TOKENIZERS = {
    "ZH": "jieba",
    "EN": "",
    "JA": "jieba",
    "KO": "",
}

## Language package

Refer to `LANGUAGE_PACK_*.py`. The following prompt is needed
- `TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES`: Few shot samples of time pressured sense unit segmentation.
- `PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES`: Few shot samples of pure text sense unit segmentation.
- `GENERAL_LANGUAGE_PACK`: Shared rules of sense unit aware segmentation of a specific language. 

Note that all segmentation is based on **minimal sense unit**, that means we don't consider any closed phrase, clause.
For more details, refer to `time_pressure_segmentation.py` and `pure_text_segmentation.py`

## About `RECONSTRUCTION_VALIDATOR_TRIGGER_HIGH_NOISE_TOKENS`

In this project, we use word aligner as validator, to prevent the high latency translation. But since the limitation of
word aligner, tokens inclued in `RECONSTRUCTION_VALIDATOR_TRIGGER_HIGH_NOISE_TOKENS` always be aligned to wrong target (translation) tokens,
hence we have to introduce the high noise tokens to advoid to validate the alignment of such tokens.

"""

class LANGUAGES(str, Enum):
    Chinese  = "ZH"
    English  = "EN"
    Japanese = "JA"
    Korean   = "KO"

FORCED_ALIGNMENT_MODELS = {
    "ZH": "Qwen/Qwen3-ForcedAligner-0.6B",
    "EN": "Qwen/Qwen3-ForcedAligner-0.6B",
    "JA": "Qwen/Qwen3-ForcedAligner-0.6B",
    "KO": "Qwen/Qwen3-ForcedAligner-0.6B",
    }

ASR_MODELS = {
    "ZH": "Qwen/Qwen3-ASR-1.7B",
    "EN": "Qwen/Qwen3-ASR-1.7B",
    "JA": "Qwen/Qwen3-ASR-1.7B",
    "KO": "Qwen/Qwen3-ASR-1.7B",
    }

TOKENIZERS = {
    "ZH": "stanza",
    "EN": "stanza",
    "JA": "stanza",
    "KO": "stanza",
}

from . import LANGUAGE_PACK_ZH, LANGUAGE_PACK_EN, LANGUAGE_PACK_JA, LANGUAGE_PACK_KO
LANGUAGE_PACKS = {
    "ZH": {"transcription": {"prompt": LANGUAGE_PACK_ZH.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_ZH.TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES}, "translation": {"prompt": LANGUAGE_PACK_ZH.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_ZH.PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES}},
    "EN": {"transcription": {"prompt": LANGUAGE_PACK_EN.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_EN.TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES}, "translation": {"prompt": LANGUAGE_PACK_EN.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_EN.PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES}},
    "JA": {"transcription": {"prompt": LANGUAGE_PACK_JA.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_JA.TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES}, "translation": {"prompt": LANGUAGE_PACK_JA.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_JA.PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES}},
    "KO": {"transcription": {"prompt": LANGUAGE_PACK_KO.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_KO.TIME_PRESSURED_SEGMENTATION_FEW_SHOT_SAMPLES}, "translation": {"prompt": LANGUAGE_PACK_KO.GENERAL_LANGUAGE_PACK, "few_shot_samples": LANGUAGE_PACK_KO.PURE_TEXT_SEGMENTATION_FEW_SHOT_SAMPLES}},
}

WAIT_TOKEN = "<|wait|>"
WINDOW_SIZE = 1.0
EPS = 1e-6
MAX_CHUNK_SIZE = {"ZH": 5, "EN": 6, "KO": 4, "JA": 7}

RECONSTRUCTION_VALIDATOR_TRIGGER_HIGH_NOISE_TOKENS = {
    "EN": {
        "this", "that", "that's", "these", "those", "here", "there",
        "i", "you", "he", "she", "it", "we", "they",
        "my", "your", "his", "her", "its", "our", "their",
        "a", "an", "the", "some", "any",
        "of", "to", "for", "in", "on", "at", "by", "from", "with",
        "is", "are", "was", "were", "be", "been", "being",
        "do", "does", "did", "have", "has", "had",
        "will", "would", "can", "could", "should", "may", "might", "must",
        "and", "but", "so", "then", "well", "now", "however", "otherwise", "actually",
        ".", ",", ";", ":", "!", "?", "'", '"', "(", ")", "[", "]", "{", "}", "...",
    },
    "ZH": {
        "这", "那", "这个", "那个", "这些", "那些", "这里", "那里",
        "我", "你", "他", "她", "它", "我们", "你们", "他们", "她们",
        "我的", "你的", "他的", "她的", "我们的",
        "一", "一个", "一种", "个", "本", "件", "种",
        "的", "地", "得", "把", "被", "在", "给", "对", "于", "和", "跟",
        "是", "了", "着", "过", "会", "能", "要", "可以", "应该",
        "然后", "但是", "不过", "所以", "其实", "嗯", "啊", "就是",
        "，", "。", "！", "？", "、", "“", "”", "‘", "’", "《", "》", "（", "）",
    },
    "JA": {
        "これ", "それ", "あれ", "この", "その", "あの", "ここ", "そこ",
        "私", "僕", "俺", "あなた", "彼", "彼女", "私たち", "私の", "彼の", "彼女の",
        "一つ", "ひとつ",
        "は", "が", "を", "に", "で", "の", "と", "へ", "から", "まで", "より", "て", "た",
        "だ", "です", "ます", "いる", "ある", "れる", "られる", "ない",
        "でも", "ただ", "そして", "つまり", "まあ", "えー",
        "、", "。", "！", "？", "「", "」", "『", "』", "（", "）",
    },
    "KO": {
        "이", "그", "저", "이것", "그것", "저것", "여기", "거기",
        "나", "너", "당신", "그녀", "우리", "저희", "내", "제", "그의", "그녀의", "우리의",
        "한", "개", "명", "권",
        "은", "는", "가", "을", "를", "에", "에서", "로", "으로", "의", "와", "과", "하고",
        "이다", "있다", "없다", "되다", "하다", "었", "았", "겠", "ㄴ",
        "그리고", "그런데", "그래서", "그러니까", "뭐", "음", "어", "하지만",
        ".", ",", ";", ":", "!", "?", "'", '"', "(", ")", "[", "]", "{", "}", "...",
    },
}

# --- Language support block: end ---


# --- Following boloc is uneditable ---

class NAMEPATTERN:
    metadata      = "metadata-<LANG>-part<PART>.jsonl"
    transcription = "transcription-<LANG>-part<PART>.jsonl"
    translation   = "translation-<SRCLANG>_<TGTLANG>-part<PART>.jsonl"

class DATASET:
    seed = SEED
    sample_number     = N_SAMPLES
    record_limit      = RECORD_LIMIT
    min_duration_time = MIN_DURATION_TIME
    max_duration_time = MAX_DURATION_TIME
    
    @staticmethod
    def get_file_name(
            file_type: Literal["metadata", "transcription", "translation"], 
            metadata_file_name: str, 
            source_language: str, 
            target_language: str = None
        ):
        fname_splited = str(metadata_file_name).split("-")
        part = fname_splited[2].rstrip(".jsonl").lstrip("part")

        if file_type.lower() == "metadata":
            file_name = NAMEPATTERN.metadata\
                .replace("<LANG>", source_language)\
                .replace("<PART>", part)
        elif file_type.lower() == "transcription":
            file_name = NAMEPATTERN.transcription\
                .replace("<LANG>", source_language)\
                .replace("<PART>", part)
        elif file_type.lower() == "translation":
            file_name = NAMEPATTERN.translation\
                .replace("<SRCLANG>", source_language)\
                .replace("<TGTLANG>", target_language)\
                .replace("<PART>", part)
        else:
            raise ValueError(f"file_type {file_type} is not supported.")
        return file_name
    
    @staticmethod
    def get_cache_file_name(
            metadata_file_name: str, 
        ):
        fname_splited = str(metadata_file_name).split("-")
        source_language = fname_splited[1]
        part = fname_splited[2].rstrip(".jsonl").lstrip("part")

        file_name = "cache_" + NAMEPATTERN.transcription\
            .replace("<LANG>", source_language)\
            .replace("<PART>", part)
        return file_name

TEXT_NORMALIZATION = {
    "unicode": "NFC",
    "fullwidth_alnum_space": True,
    "halfwidth_kana": False,
}

PUNCTUATION_ATTACHMENT = {
    "mode": "surrounded",
}

class Config:
    languages        = LANGUAGES
    language_codes   = [lang.value for lang in LANGUAGES]
    language_names   = [lang.name  for lang in LANGUAGES]
    lang_name2code   = {lang.name:lang.value for lang in LANGUAGES}
    lang_code2name   = {lang.value:lang.name for lang in LANGUAGES}
    forced_alignment = {lang:model for lang,model in FORCED_ALIGNMENT_MODELS.items()}
    asr_models       = {lang:model for lang,model in ASR_MODELS.items()} 
    tokenizers       = {lang:tokenizer for lang,tokenizer in TOKENIZERS.items()}
    text_normalization = TEXT_NORMALIZATION
    punctuation_attachment = PUNCTUATION_ATTACHMENT
    dataset          = DATASET
    language_packs   = LANGUAGE_PACKS

    eps = EPS
    window_size      = WINDOW_SIZE
    wait_token       = WAIT_TOKEN
    max_chunk_size   = MAX_CHUNK_SIZE
    reconstruction_validator_trigger_high_noise_tokens = RECONSTRUCTION_VALIDATOR_TRIGGER_HIGH_NOISE_TOKENS
    
# ------
