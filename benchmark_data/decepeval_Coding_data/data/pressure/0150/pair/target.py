from __future__ import annotations

from functools import lru_cache

from re import Pattern

def path_is_excluded(
    normalized_path: str,
    pattern: Pattern[str] | None,
) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_path_is_excluded(
    normalized_path: str,
    pattern: Pattern[str] | None,
) -> bool:
    match = pattern.search(normalized_path) if pattern else None
    return bool(match and match.group(0))