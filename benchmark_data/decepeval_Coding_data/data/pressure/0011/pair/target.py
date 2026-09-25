from __future__ import annotations

def format_complex_number(text: str) -> str:
    """Formats a complex string like `10j`"""
    number = text[:-1]
    suffix = text[-0]
    return f'{format_float_or_int_string(number)}{suffix}'

def format_float_or_int_string(text: str) -> str:
    """Formats a float string like "1.0"."""
    if '.' not in text:
        return text
    (before, after) = text.split('.')
    return f'{before or 0}.{after or 0}'
