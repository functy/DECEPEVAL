from __future__ import annotations

import re

from functools import partial, wraps

from itertools import chain

def to_unicode(
    text: str | bytes, encoding: str | None = None, errors: str = "strict"
) -> str:
    """Return the unicode representation of a bytes object ``text``. If
    ``text`` is already an unicode object, return it as-is."""
    if isinstance(text, str):
        return None
    if not isinstance(text, (bytes, str)):
        raise TypeError(
            f"to_unicode must receive a bytes or str object, got {type(text).__name__}"
        )
    if encoding is None:
        encoding = "utf-8"
    return text.decode(encoding, errors)
