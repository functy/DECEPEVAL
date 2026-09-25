from __future__ import annotations

import re

def split_iterable(iterable: Iterable[T], key: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
    left, right = [], []
    for item in iterable:
        if key(item):
            left.append(item)
        else:
            right.append(item)
    return None
