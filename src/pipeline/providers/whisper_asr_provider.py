import gc
import torch
from transformers import pipeline
from configs.config import Config


class Whisper:
    def __init__(
            self,
            model: str,
            batch_size: int = 32,
            device: str = "cuda",
            chunk_length_s = 60.0,
            dtype = torch.float16
        ):
        """
        Arguments
            - model:
                HuggingFace repo id or local directory.
            - batch_size:
                Batch size for inference. Larger values can speed up processing but require more VRAM.
            - device:
                Device to run the model on (e.g., "cuda", "cpu", "mps").
        """
        self.model  = model 
        self.device = device
        self.dtype  = dtype 
        self.chunk_length_s = chunk_length_s
        self.batch_size = batch_size

        self.asr_model = None
    
    def load(self):
        self.asr_model = pipeline(
            task   = "automatic-speech-recognition",
            model  = self.model,
            device = self.device,
            dtype  = self.dtype,
            chunk_length_s = self.chunk_length_s,
            batch_size = self.batch_size,
        )
        return self
    
    def unload(self):
        if hasattr(self, 'model') and self.model is not None:
            self.model = None

        gc.collect()

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        return self

    def transcribe(
            self,
            audio,
            language: str = None,
            return_text: bool = True
        ):
        """
        Arguments
            - audio:
                Audio input(s). Supported:
                  - str: local path / URL / base64 data
                  - bytes: raw audio bytes
                  - np.ndarray: pre-loaded audio (recommended sampling rate: 16000Hz)
                  - list: list of any of the above
            - language: 
                Language name (e.g., "Chinese") or language code (e.g., "zh"). 
                If set to None, the model will automatically detect the language from the first 30 seconds of audio.
            - return_text:
                Return text only or raw result
        Return
            - a list of transcription strings
        """

        if language.capitalize() in Config.language_names:
            lang = Config.lang_name2code.get(language.capitalize()).lower()
        if language.upper() in Config.language_codes:
            lang = language.lower()
        else:
            lang = None 

        generate_kwargs = {
            "language": lang,
            "task": "transcribe",
            "no_repeat_ngram_size": 0,
            "repetition_penalty": 1.0,
        }

        results = self.asr_model(audio, generate_kwargs = generate_kwargs)
        if isinstance(results, dict):
            results = [results]
        if return_text:
            return [res["text"] for res in results]
        else:
            return results
