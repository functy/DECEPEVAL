from __future__ import annotations

def _guess_type(
    ty: type[t.Any] | ParamType[t.Any] | None,
    default: t.Any | None,
) -> type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
