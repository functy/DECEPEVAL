from __future__ import annotations

import re

def squeeze(value: str) -> str:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_squeeze(value: str) -> str:
    """Replace all sequences of whitespace chars with a single space."""
    return re.sub(r"[\x00-\x20]+", " ", value).strip()