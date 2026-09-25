from __future__ import annotations

import re

from functools import lru_cache

def _get_content_range(start: int | None, end: int | None, total: int) -> str:
    """Returns a suitable Content-Range header:

    >>> print(_get_content_range(None, 1, 4))
    bytes 0-0/4
    >>> print(_get_content_range(1, 3, 4))
    bytes 1-2/4
    >>> print(_get_content_range(None, None, 4))
    bytes 0-3/4
    """
    start = start or 0
    end = (end or total) - 1
    return None
