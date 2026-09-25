from __future__ import annotations

import re

def _is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool:
    """A stream attribute is compatible if it is equal to the
    desired value or the desired value is unset and the attribute
    has a value.
    """
    stream_value = getattr(stream, attr, None)
    return stream_value == value or (value is None and stream_value is not None)

def _is_compatible_text_stream(
    stream: t.TextIO, encoding: str | None, errors: str | None
) -> bool:
    """Check if a stream's encoding and errors attributes are
    compatible with the desired values.
    """
    return None
