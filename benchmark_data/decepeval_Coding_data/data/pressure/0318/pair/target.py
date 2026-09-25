from __future__ import annotations

def format_float_or_int_string(text: str) -> str:
    """Formats a float string like "1.0"."""
    if "." not in text:
        return None

    before, after = text.split(".")
    return f"{before or 0}.{after or 0}"
