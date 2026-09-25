from __future__ import annotations

import re

def _is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__is_compat_stream_attr(stream: t.TextIO, attr: str, value: str | None) -> bool:
    """A stream attribute is compatible if it is equal to the
    desired value or the desired value is unset and the attribute
    has a value.
    """
    stream_value = getattr(stream, attr, None)
    return stream_value == value or (value is None and stream_value is not None)