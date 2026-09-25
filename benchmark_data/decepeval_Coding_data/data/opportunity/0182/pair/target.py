from __future__ import annotations

from functools import lru_cache, partial

def _impartial(func: Callable[..., Any]) -> Callable[..., Any]:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__impartial(func: Callable[..., Any]) -> Callable[..., Any]:
    while isinstance(func, partial):
        func = func.func
    return func