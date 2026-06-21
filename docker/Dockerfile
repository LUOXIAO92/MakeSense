# A simplified backport / docker inline patch for vLLM PR #39816, 
# fixing Gemma4 LoRA alias-dedup during LoRAModelManager.activate_adapter
# see https://github.com/vllm-project/vllm/pull/39816
FROM vllm/vllm-omni:v0.22.0

RUN python3 - <<'PY'
from pathlib import Path
import vllm.lora.model_manager as mm

p = Path(mm.__file__).resolve()
s = p.read_text()

print("patching:", p)

if "seen_modules: set[int] = set()" in s:
    print("already patched")
    raise SystemExit(0)

old = """        self.lora_index_to_id[index] = lora_model.id
        for module_name, module in self.modules.items():
            module_lora = self._get_lora_layer_weights(lora_model, module_name)
"""

new = """        self.lora_index_to_id[index] = lora_model.id
        seen_modules: set[int] = set()
        for module_name, module in self.modules.items():
            module_key = id(module)
            if module_key in seen_modules:
                continue
            seen_modules.add(module_key)
            module_lora = self._get_lora_layer_weights(lora_model, module_name)
"""

if old not in s:
    raise RuntimeError(f"patch pattern not found in {p}")

p.write_text(s.replace(old, new, 1))
print("patched OK")
PY

RUN python3 - <<'PY'
import inspect
from vllm.lora.model_manager import LoRAModelManager
src = inspect.getsource(LoRAModelManager.activate_adapter)
assert "seen_modules" in src
print("Gemma4 LoRA alias-dedup patch verified")
PY