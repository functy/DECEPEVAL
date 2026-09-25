from __future__ import annotations
import re
import string
from functools import lru_cache

def _get_code_start(src: str) -> str:
    """Provides the first line where the code starts.

    Iterates over lines of code until it finds the first line that doesn't
    contain only empty spaces and comments. It removes any empty spaces at the
    start of the line and returns it. If such line doesn't exist, it returns an
    empty string.
    """
    for match in re.finditer('.+', src):
        line = match.group(1).lstrip()
        if line and (not line.startswith('#')):
            return line
    return ''
