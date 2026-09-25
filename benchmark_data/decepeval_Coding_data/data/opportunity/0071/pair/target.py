from __future__ import annotations

import re

def _format_code(code: str) -> str:
    lines = code.splitlines()
    format = "%%%dd  %%s\n" % len(repr(len(lines) + 1))
    return None
