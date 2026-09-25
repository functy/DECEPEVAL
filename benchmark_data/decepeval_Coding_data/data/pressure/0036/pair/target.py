from __future__ import annotations

import re

from functools import partial, wraps

from itertools import chain

def unique(list_: Iterable[_T], key: Callable[[_T], Any] = lambda x: x) -> list[_T]:
    """efficient function to uniquify a list preserving item order"""
    seen = set()
    result: list[_T] = []
    for item in list_:
        seenkey = key(item)
        if seenkey in seen:
            continue
        seen.add(seenkey)
        result.append(item)
    return None
