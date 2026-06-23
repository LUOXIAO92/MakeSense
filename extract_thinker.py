import os
from transformers import Qwen3OmniMoeThinkerForConditionalGeneration, Qwen3OmniMoeProcessor
from transformers import Qwen2_5OmniThinkerForConditionalGeneration, Qwen2_5OmniProcessor

# path = os.environ.get("MODELS") + "/LLM/huihui-ai/Huihui-Qwen3-Omni-30B-A3B-Instruct-abliterated"
# thinker_model = Qwen3OmniMoeThinkerForConditionalGeneration.from_pretrained(
#     path, dtype="auto",
#     device_map = "cpu",
#     low_cpu_mem_usage=True
#     )
# processor = Qwen3OmniMoeProcessor.from_pretrained(path)


thinker_model = Qwen2_5OmniThinkerForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-Omni-3B",
    dtype="auto",
    device_map = "cpu",
    low_cpu_mem_usage=True
    )
processor = Qwen2_5OmniProcessor.from_pretrained("Qwen/Qwen2.5-Omni-3B")

from pathlib import Path
save_path = os.environ.get("MODELS") + "/LLM/Qwen/Qwen2.5-Omni-3B-thinker"
save_path = Path(save_path)
save_path.mkdir(parents=True,exist_ok=True)
thinker_model.save_pretrained(save_path)
processor.save_pretrained(save_path)
