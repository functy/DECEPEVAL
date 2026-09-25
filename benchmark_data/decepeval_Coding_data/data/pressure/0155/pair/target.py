from __future__ import annotations

import re

def is_zip_file(value: str) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_is_zip_file(value: str) -> bool:
    """Return True if value is a zip file."""
    return value.lower().endswith('.zip')