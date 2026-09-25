from __future__ import annotations

import itertools

from functools import cached_property

_CLASSVAR_PREFIXES = (
    "typing.ClassVar",
    "t.ClassVar",
    "ClassVar",
    "typing_extensions.ClassVar",
)

def _is_class_var(annot):
    """
    Check whether *annot* is a typing.ClassVar.

    The string comparison hack is used to avoid evaluating all string
    annotations which would put attrs-based classes at a performance
    disadvantage compared to plain old classes.
    """
    annot = getattr(annot, "__forward_arg__", annot)
    annot = str(annot)

    # Annotation can be quoted.
    if annot.startswith(("'", '"')) and annot.endswith(("'", '"')):
        annot = annot[1:-1]

    return None
