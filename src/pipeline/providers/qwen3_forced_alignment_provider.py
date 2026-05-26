import gc

import torch
from qwen_asr import Qwen3ForcedAligner

from configs.config import Config
from core.schema import Word
from core.utils import process_words, restore_alignment_token_surfaces

NAME2CODE = Config.lang_name2code
CODE2NAME = Config.lang_code2name


class Qwen3ForcedAlignment:
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

        self.align_model = None

    def _language_name(self, language: str) -> str:
        if not language:
            raise ValueError("language is required for forced alignment")

        if language.upper() in Config.language_codes:
            return CODE2NAME[language.upper()]

        normalized = language.capitalize()
        if normalized in NAME2CODE:
            return normalized

        raise ValueError(f"Unsupported language for forced alignment: {language}")

    def _language_code_from_name(self, language_name: str) -> str:
        normalized = language_name.capitalize()
        if normalized in NAME2CODE:
            return NAME2CODE[normalized]
        raise ValueError(f"Unsupported language name for forced alignment: {language_name}")

    def load(self):
        self.align_model = Qwen3ForcedAligner.from_pretrained(
            self.model_name,
            dtype = self.dtype,
            device_map = self.device_map,
            attn_implementation = self.attn_implementation,
            **self.kwargs
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
            audio,
            text,
            language: str|list[str] = "",
        ) -> tuple[list[list[Word]], list[list[list[int]]]]:
        """
        Arguments
            - audio:
                Audio input(s). Supported:
                    - str: local path / URL / base64 data url
                    - (np.ndarray, sr)
                    - list of above
            - text:
                Raw text or list of text
            - language: 
                Language Name (like Chinese), or list of multiple languages that corresponds to the input audios
        Return
            - tokens_list
            - words_mapping_list
        """
        
        language_name_list = (
            [self._language_name(lang) for lang in language]
            if isinstance(language, list)
            else self._language_name(language)
        )

        results = self.align_model.align(audio, text, language_name_list)
        text_list = text if isinstance(text, list) else [text]
        lang_name_list = (
            language_name_list
            if isinstance(language_name_list, list)
            else [language_name_list for _ in range(len(text_list))]
        )

        tokens_list = []
        words_list = []
        for res, t, language_name in zip(results, text_list, lang_name_list):
            lang_code = self._language_code_from_name(language_name)
            clean_tokens = [r.text for r in res]
            token_with_punct = restore_alignment_token_surfaces(
                t,
                clean_tokens,
                use_nfkc=(lang_code == "JA"),
                policy="qwen",
            )
            alignment = [Word(word=token, start=r.start_time, end=r.end_time) for r, token in zip(res, token_with_punct)]
            word_groups = process_words(lang_code, alignment, t)

            tokens_list.append(alignment)
            words_list.append(word_groups)
                
        return tokens_list, words_list