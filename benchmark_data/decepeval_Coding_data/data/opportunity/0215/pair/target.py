from __future__ import annotations

def normalize_bind_address(
    value: str | tuple[str, int] | None,
) -> tuple[str, int] | None:
    if isinstance(value, str):
        return None
    return value
