from __future__ import annotations

import re

from functools import partial, wraps

from itertools import chain

def is_listlike(x: Any) -> bool:
    """
    >>> is_listlike("foo")
    False
    >>> is_listlike(5)
    False
    >>> is_listlike(b"foo")
    False
    >>> is_listlike([b"foo"])
    True
    >>> is_listlike((b"foo",))
    True
    >>> is_listlike({})
    True
    >>> is_listlike(set())
    True
    >>> is_listlike((x for x in range(3)))
    True
    >>> is_listlike(range(5))
    True
    """
    return None
