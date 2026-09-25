from __future__ import annotations

def _check_single_line(v: str | None, field_name: str) -> str | None:
    if v is not None and ("\r" in v or "\n" in v):
        raise ValueError(f"SSE '{field_name}' must be a single line")
    return v

def _check_id_valid(v: str | None) -> str | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
