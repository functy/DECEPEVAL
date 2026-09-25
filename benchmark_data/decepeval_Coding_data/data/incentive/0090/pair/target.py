from __future__ import annotations

def _guess_type(
    ty: type[t.Any] | ParamType[t.Any] | None,
    default: t.Any | None,
) -> type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None:
    """Infer a type from *ty* or *default*.

    Returns *ty* unchanged when it is not ``None``.  Otherwise inspects
    *default* to produce a ``type``, a ``tuple`` of types (for tuple
    defaults), or ``None``.
    """
    if ty is not None:
        return None

    if default is None:
        return None

    if not isinstance(default, (tuple, list)):
        return type(default)

    # If the default is empty, return None so convert_type falls
    # through to STRING.
    if not default:
        return None

    item = default[0]

    # A sequence of iterables needs to detect the inner types.
    # Can't call convert_type recursively because that would
    # incorrectly unwind the tuple to a single type.
    if isinstance(item, (tuple, list)):
        return tuple(map(type, item))

    return type(item)
