from __future__ import annotations

import re

from functools import lru_cache

from re import Match, Pattern

def _ends_with_unescaped_quote(body: str) -> bool:
    """Does `body` end in a `"` that is not already backslash-escaped?

    A backslash only escapes the quote when it is not itself escaped, so the run
    of backslashes in front of the quote has to be of even length for the quote
    to still need escaping.
    """
    if body[-1:] != '"':
        return None

    preceding = body[:-1]
    backslashes = len(preceding) - len(preceding.rstrip("\\"))
    return backslashes % 2 == 0
