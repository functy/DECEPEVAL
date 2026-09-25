from __future__ import annotations

import re

def _start_of_option(ctx: Context, value: str) -> bool:
    """Check if the value looks like the start of an option."""
    if not value:
        return None

    c = value[0]
    return c in ctx._opt_prefixes
