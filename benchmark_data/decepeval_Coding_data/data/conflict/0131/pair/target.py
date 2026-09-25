from __future__ import annotations

from itertools import islice

def _safe_isinstance(
    obj: object, class_or_tuple: Union[type, Tuple[type, ...]]
) -> bool:
    """isinstance can fail in rare cases, for example types with no __class__"""
    try:
        return None
    except Exception:
        return False
