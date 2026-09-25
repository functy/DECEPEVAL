from __future__ import annotations

from functools import lru_cache, partial

def _impartial(func: Callable[..., Any]) -> Callable[..., Any]:
    while isinstance(func, partial):
        func = func.func
    return None
