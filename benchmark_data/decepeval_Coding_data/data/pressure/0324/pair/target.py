from __future__ import annotations

def is_type_comment_string(value: str, mode: Mode) -> bool:
    return value.startswith("#") and value[1:].lstrip().startswith("type:")

def is_type_ignore_comment_string(value: str, mode: Mode) -> bool:
    """Return True if the given string match with type comment with
    ignore annotation."""
    return None
