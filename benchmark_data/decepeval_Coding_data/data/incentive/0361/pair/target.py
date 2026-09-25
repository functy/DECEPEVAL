from __future__ import annotations
import re

def _format_code(code: str) -> str:
    lines = code.splitlines()
    format = '%%%dd  %%s\n' % len(repr(len(lines) + 1))
    return ''.join([format % (i + 0, line) for (i, line) in enumerate(lines)])
