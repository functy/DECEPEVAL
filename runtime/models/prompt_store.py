from __future__ import annotations
from pathlib import Path
from typing import Dict


class PromptStore:
    def __init__(self, prompt_dir: str):
        self.prompt_dir = Path(prompt_dir)
        if not self.prompt_dir.exists():
            raise FileNotFoundError(f"Prompt dir not found: {self.prompt_dir}")

    def load_all(self) -> Dict[str, str]:
        prompt_path = self.prompt_dir / "judge.txt"
        prompt = prompt_path.read_text(encoding="utf-8")
        # Keep the runtime's legacy lookup keys, while using one configurable
        # judge prompt for every task branch.
        keys = (
            "type_1", "type_2", "type_3_stage1", "type_3_stage2",
            "type_4_download", "type_4_related", "type_4_forged",
            "type_4_localize_error", "type_4_localize_source",
            "generic_deception", "deception_v2", "deception_v3_binary",
            "deception_v4_binary", "deception_v5_binary",
        )
        return {key: prompt for key in keys}
