from __future__ import annotations

import functools

def trim_release(release: tuple[int, ...]) -> tuple[int, ...]:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_trim_release(release: tuple[int, ...]) -> tuple[int, ...]:
    """Strip trailing zeros from a release tuple for normalized comparison."""
    end = len(release)
    while end > 1 and release[end - 1] == 0:
        end -= 1
    return release if end == len(release) else release[:end]