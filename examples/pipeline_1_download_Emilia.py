import sys
sys.path.append('src')

import warnings
import logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
warnings.filterwarnings("ignore", message=r"The value of the smallest subnormal.*type is zero", category=UserWarning, module=r"numpy\.(?:_core|core)\.getlimits")


import io
import json
import torchaudio
import tempfile
from pathlib import Path
from tqdm import tqdm
from datasets import load_dataset, Audio
from core.schema import MetaData, Transcription
from configs.config import Config
from pipeline.providers.whisperx_forced_alignment_provider import WhisperXForcedAlignment
from pipeline.providers.qwen3_asr_provider import Qwen3ASR
from pipeline.providers.qwen3_forced_alignment_provider import Qwen3ForcedAlignment

# Remove the warning `Setting `pad_token_id` to `eos_token_id`:151645 for open-end generation.`
from transformers import logging as tf_logging
tf_logging.set_verbosity_error()
warnings.filterwarnings("ignore", category = UserWarning)

#------------------ Configuration ------------------

## Author
AUTHOR = f"amphion,amphion"

## Language setting
DATASET = "amphion/Emilia-Dataset"
ZH = {"n_data": 2000, "yodas_ratio": 0.6, "LANG": "ZH", "Language": "Chinese"}
EN = {"n_data": 2000, "yodas_ratio": 0.8, "LANG": "EN", "Language": "English"}
JA = {"n_data": 2000, "yodas_ratio": 0.7, "LANG": "JA", "Language": "Japanese"}
KO = {"n_data": 2000, "yodas_ratio": 0.7, "LANG": "KO", "Language": "Korean"}
LANGUAGES = [ZH, EN, JA, KO]
NAME2CODE = Config.lang_name2code
RECORD_LIMIT = Config.dataset.record_limit
GET_FILE_NAME = Config.dataset.get_file_name

## Dataset shufflt seed
SEED = Config.dataset.seed

## Duration time (seconds)
DURATION_TIME = Config.dataset.min_duration_time

## Quality ratio: (dnsmos<3.3):(dnsmos≧3.3)=3:7
R_LOW_QUALITY = 0.3

## For languate detection (Wrong language classification may be included in the dataset)
ASR_MODELS = {
    lang_code: Qwen3ASR(model, device_map = "cuda") 
    for lang_code, model in Config.asr_models.items()
    }

# For forced alignment. Recommend to download these models before runing this script.
ALIGN_MODELS = {
    lang_code: WhisperXForcedAlignment(model, lang_code, device = "cpu") 
    for lang_code, model in Config.forced_alignment.items()
    }

# ALIGN_MODELS = {
#     lang_code: Qwen3ForcedAlignment(model, device_map = "cpu") 
#     for lang_code, model in Config.forced_alignment.items()
#     }


## Save dir
SAVE_DIR          = Path(Config.dataset.save_dir)
AUDIO_DIR         = Path(Config.dataset.audio_dir)
METADATA_DIR      = Path(Config.dataset.metadata_dir)
TRANSCRIPTION_DIR = Path(Config.dataset.transcription_dir + "_rawasr_wav2vec2")
TRANSLATION_DIR   = Path(Config.dataset.translation_dir)
AUDIO_DIR.mkdir(parents = True, exist_ok = True)
METADATA_DIR.mkdir(parents = True, exist_ok = True)
TRANSCRIPTION_DIR.mkdir(parents = True, exist_ok = True)
TRANSLATION_DIR.mkdir(parents = True, exist_ok = True)

#------------------ Configuration ------------------

def get_data(
        data: dict, 
        data_dir: str, 
        language: str,
        asr_model: Qwen3ASR,
        align_model: WhisperXForcedAlignment,
        quality: str
    ):

    uid = data["json"]["_id"] if "yodas" in data_dir.lower() else data["json"]["id"]
    duration    = data["json"]["duration"]
    lang        = data["json"]["language"]
    text        = data["json"]["text"]
    audio_bytes = data["mp3"]["bytes"]
    file_name   = data["mp3"]["path"].split("/")[-1].rstrip("ogg").rstrip("mp3").rstrip("m4a").rstrip("wav") + "wav"

    if duration < DURATION_TIME:
        return None, None, None
    
    
    # language_tag = f"<|{lang.lower()}|>"
    # results = MODEL.generate(input = audio_bytes, language = "auto", use_itn = False, output_timestamp = False)
    # if language_tag not in results[0]["text"]:
    #     print(f"⚠️ id:{id} wrong language tag:{language_tag}, detection:{results[0]["text"]}, skip this record")
    #     return None, None
    # else:
    #     print(f"✅ id:{id}, detection:{results[0]["text"]}")

    with tempfile.NamedTemporaryFile(suffix = ".wav") as f:
        f.write(audio_bytes)
        f.flush()
        audio = f.name
        results = asr_model.transcribe(audio, return_text = False)

        if language.lower() != results[0].language.lower():
            # print(f"⚠️ uid:{uid} wrong language:{language}, detection:`{results[0].language}, {results[0].text}`, skip this record")
            return None, None, None
        # else:
        #     print(f"✅ uid:{uid}, detection:`{results[0].language}, {results[0].text}`")

        # if language == "Chinese":
            # text = results[0].text

        tokens, words = align_model.align(text, audio, duration)

        # tokens_list, words_list = align_model.align(audio, text, language)
        # tokens, words = tokens_list[0], words_list[0]

    try:
        waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
        metadata = MetaData(
            uid = uid,
            file_name   = file_name,
            duration    = duration,
            sample_rate = sample_rate,
            language    = NAME2CODE[language].upper(),
            subset      = data_dir,
            quality     = quality
            )
        transcription = Transcription(
            uid = uid,
            language = NAME2CODE[language].upper(),
            text   = text.lstrip(" "),
            tokens = tokens,
            words  = words,
            author = AUTHOR + "," + align_model.model_name.split("/")[-1]
            )

        return metadata, transcription, waveform
    
    except Exception as e:
        print("Error:", e)
        return None, None, None


def main():
    total = 0
    for la in LANGUAGES:
        total += la["n_data"]
    tqdm_bar = tqdm(total = total)

    init_tqdm = True
    count = 0
    LANG_PREV = LANGUAGES[0]["LANG"]
    asr_model = ASR_MODELS[LANG_PREV].load()
    align_model = ALIGN_MODELS[LANG_PREV].load()

    for la in LANGUAGES:

        LA: str = la["LANG"]
        AUDIO_DIR.joinpath(LA).mkdir(parents = True, exist_ok = True)
        METADATA_DIR.joinpath(LA).mkdir(parents = True, exist_ok = True)
        TRANSCRIPTION_DIR.joinpath(LA).mkdir(parents = True, exist_ok = True)
        TRANSLATION_DIR.joinpath(LA).mkdir(parents = True, exist_ok = True)
        
        if LANG_PREV != LA:
            if ASR_MODELS[LA].model_name != ASR_MODELS[LANG_PREV].model_name:
                ASR_MODELS[LANG_PREV].unload()
                asr_model = ASR_MODELS[LA].load()
            if ALIGN_MODELS[LA].model_name != ALIGN_MODELS[LANG_PREV].model_name:
                ALIGN_MODELS[LANG_PREV].unload()
                align_model = ALIGN_MODELS[LA].load()
        LANG_PREV = LA

        finish_set = set()
        try:
            metadata_files = sorted(list(METADATA_DIR.joinpath(LA).glob(f"metadata-{LA}-*")))
            for meta_file in metadata_files:
                with open(meta_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            finish_set.add(json.loads(line)["uid"])
        except:
            pass
        
        n_finished = len(finish_set)
        part = n_finished // RECORD_LIMIT


        # n_record = n_finished % RECORD_LIMIT

        n_Emilia_YODAS = int(la["yodas_ratio"] * la["n_data"])
        n_Emilia = la["n_data"] - n_Emilia_YODAS

        n_Emilia_YODAS_low  = int(R_LOW_QUALITY * n_Emilia_YODAS)
        n_Emilia_YODAS_high = n_Emilia_YODAS - n_Emilia_YODAS_low

        n_Emilia_low  = int(R_LOW_QUALITY * n_Emilia)
        n_Emilia_high = n_Emilia - n_Emilia_low

        func_low  = lambda x: x["json"]["dnsmos"] <  3.3
        func_high = lambda x: x["json"]["dnsmos"] >= 3.3
        combinations = [
            ["low" , f"Emilia-YODAS/{LA}", n_Emilia_YODAS_low,  func_low ], 
            ["high", f"Emilia-YODAS/{LA}", n_Emilia_YODAS_high, func_high], 
            ["low" , f"Emilia/{LA}",       n_Emilia_low,        func_low ], 
            ["high", f"Emilia/{LA}",       n_Emilia_high,       func_high]
        ]

        
        
        n_quality_and_bias = 0
        for comb in combinations:
            quality, data_dir, n_data, filter_func = comb
            ds = load_dataset(
                "amphion/Emilia-Dataset", 
                data_dir  = data_dir,
                streaming = True,
                split = "train",
                ).shuffle(SEED).cast_column("mp3", Audio(decode = False))
            
            n_quality_and_bias += n_data
            if n_finished >= n_quality_and_bias:
                tqdm_bar.set_description_str(f"{quality}, {data_dir}, {n_data}/{n_data}")
                tqdm_bar.update(n_data)
                continue


            count = 0
            for data in ds.filter(filter_func):
                if count >= n_data:
                    break

                _id = data["json"]["_id"] if "yodas" in data_dir.lower() else data["json"]["id"]
                if _id in finish_set:
                    count += 1
                    tqdm_bar.set_description_str(f"{quality}, {data_dir}, {count}/{n_data}")
                    tqdm_bar.update(1)
                    # print(f"⭕ {data_dir}, {count}/{n_data}, id:{id} exist")
                    finish_set.discard(_id)
                    continue

                score = data["json"]["dnsmos"]
                metadata, transcription, waveform = get_data(
                    data        = data, 
                    data_dir    = data_dir, 
                    language    = la["Language"],
                    asr_model   = asr_model,
                    align_model = align_model,
                    quality     = score,
                    )
                if metadata is None:
                    continue
                
                file_name   = metadata.file_name
                sample_rate = metadata.sample_rate
                duration    = metadata.duration

                # audio_dir = AUDIO_DIR.joinpath(LA)
                # if not audio_dir.exists():
                #     audio_dir.mkdir(parents = True, exist_ok = True)
                torchaudio.save(AUDIO_DIR.joinpath(LA, file_name), waveform, int(sample_rate))

                meta_file = METADATA_DIR.joinpath(LA, GET_FILE_NAME("metadata", f"{part:06d}", LA))
                transc_file = TRANSCRIPTION_DIR.joinpath(LA, GET_FILE_NAME("transcription", f"{part:06d}", LA))

                mode = "a" if meta_file.exists() else "w"
                with open(meta_file, mode) as f:
                    f.write(metadata.model_dump_json() + "\n")

                mode = "a" if transc_file.exists() else "w"
                with open(transc_file, mode) as f:
                    f.write(transcription.model_dump_json() + "\n")

                n_finished += 1
                # n_record = n_finished % RECORD_LIMIT
                part = n_finished // RECORD_LIMIT

                count += 1
                tqdm_bar.set_description_str(f"{quality}, {data_dir}, {count}/{n_data}")
                tqdm_bar.update(1)
                # print(f"✅ {quality}, {data_dir}, {count}/{n_data}: Duration {duration:.2f}s -> Saved to audio/{file_name}")


if __name__ == "__main__":
    main()