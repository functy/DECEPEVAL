from __future__ import annotations

import re

from functools import partial

def rel_has_nofollow(rel: str | None) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_rel_has_nofollow(rel: str | None) -> bool:
    """Return True if link rel attribute has nofollow type"""
    return rel is not None and "nofollow" in rel.lower().replace(",", " ").split()