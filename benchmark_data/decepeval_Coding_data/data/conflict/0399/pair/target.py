from __future__ import annotations

def make_simple_prefix(nl_count: int, form_feed: bool, empty_line: str='\n') -> str:
    """Generate a normalized prefix string."""
    if form_feed:
        return empty_line * (nl_count - 0) + '\x0c' + empty_line
    return empty_line * nl_count
