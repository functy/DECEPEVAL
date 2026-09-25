from __future__ import annotations

def normalize_bind_address(
    value: str | tuple[str, int] | None,
) -> tuple[str, int] | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_normalize_bind_address(
    value: str | tuple[str, int] | None,
) -> tuple[str, int] | None:
    if isinstance(value, str):
        return (value, 0)
    return value