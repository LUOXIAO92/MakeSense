import gc
import torch
from typing import Optional
from configs.config import Config
from qwen_asr import Qwen3ASRModel
from qwen_asr.inference.qwen3_asr import ASRTranscription

class Qwen3ASR:
    def __init__(
            self,
            model_name: str,
            dtype = torch.bfloat16,
            device_map = "cuda",
            attn_implementation = "flash_attention_2",
            max_inference_batch_size = 32,
            max_new_tokens = 1024,
            **kwargs
        ):
        """
        Arguments
            - model_name:
                HuggingFace repo id or local directory.
            - max_inference_batch_size:
                Batch size limit for inference. -1 means no chunking. Small values can avoid OOM.
            - max_new_tokens:
                Maximum number of tokens to generate.
            - **kwargs:
                Forwarded to AutoModel.from_pretrained(...).
        """
        self.model_name = model_name
        self.dtype = dtype
        self.device_map = device_map
        self.attn_implementation = attn_implementation
        self.max_inference_batch_size = max_inference_batch_size
        self.max_new_tokens = max_new_tokens
        self.kwargs = kwargs

        self.asr_model = None

    def load(self):
        self.asr_model = Qwen3ASRModel.from_pretrained(
            self.model_name,
            dtype = self.dtype,
            device_map = self.device_map,
            attn_implementation = self.attn_implementation,
            max_inference_batch_size = self.max_inference_batch_size,
            max_new_tokens = self.max_new_tokens,
            **self.kwargs
            )
        return self
    
    def unload(self):
        if self.asr_model is not None:
            self.asr_model = None

        gc.collect()

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        return self

    def transcribe(
            self,
            audio,
            language: Optional[str] = None,
            return_text: bool = True
        ) -> list[str] | list[ASRTranscription]:
        """
        Arguments
            - audio:
                Audio input(s). Supported:
                    - str: local path / URL / base64 data url
                    - (np.ndarray, sr)
                    - list of above

            - language: 
                Language CODE or Name (like ZH or Chinese), or list of multiple languages that corresponds to the input audios
            - return_text:
                Return text only or raw result
        Return
            - a list of transcription strings
        """

        if language is not None:
            if language.capitalize() not in Config.language_names:
                lang = None 
            if language.upper() in Config.language_codes:
                lang = Config.lang_name2code.get(language.upper())
            else:
                lang = None
        else:
            lang = language
        
        results = self.asr_model.transcribe(audio, language = lang, return_time_stamps = False)

        if return_text:
            return [res.text for res in results]
        else:
            return results