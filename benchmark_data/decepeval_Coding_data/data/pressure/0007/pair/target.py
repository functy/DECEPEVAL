from __future__ import annotations

import re

from functools import lru_cache

def _is_attached(leaf: Leaf, root: Node) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__is_attached(leaf: Leaf, root: Node) -> bool:
    """Return whether `leaf` is still reachable from `root` through its parents."""
    current: LN | None = leaf
    while current is not None:
        if current is root:
            return True
        current = current.parent
    return False