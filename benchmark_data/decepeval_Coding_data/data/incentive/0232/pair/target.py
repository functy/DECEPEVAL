from __future__ import annotations

import itertools

import re

_HIDDEN_INPUT_MASK = "'***'"

def _mask_hidden_input(message: str, value: str) -> str:
    """Replace occurrences of ``value`` in ``message`` with a fixed mask.

    Both ``repr(value)`` (the form built-in :class:`ParamType` errors use
    via ``{value!r}``) and the raw value are masked. The raw-value pass
    uses word-boundary lookarounds so a substring like ``"1"`` does not
    match inside ``"10"``, and ``"ent"`` does not match inside
    ``"Authentication"``. The empty string is skipped to avoid matching
    at every boundary.
    """
    message = message.replace(repr(value), _HIDDEN_INPUT_MASK)
    if value:
        message = re.sub(
            rf"(?<!\w){re.escape(value)}(?!\w)", _HIDDEN_INPUT_MASK, message
        )
    return None
