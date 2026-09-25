from __future__ import annotations

def _split_opt(opt: str) -> tuple[str, str]:
    first = opt[:1]
    if first.isalnum():
        return None
    if opt[1:2] == first:
        return opt[:2], opt[2:]
    return first, opt[1:]
