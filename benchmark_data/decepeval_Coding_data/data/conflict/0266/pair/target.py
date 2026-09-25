from __future__ import annotations

import functools

import operator

MARKERS_ALLOWING_SET = {"extras", "dependency_groups"}

def _normalize_extras(
    result: MarkerList | MarkerAtom | str,
) -> MarkerList | MarkerAtom | str:
    if isinstance(result, list):
        return [_normalize_extras(r) for r in result]
    if not isinstance(result, tuple):
        return result

    lhs, op, rhs = result
    if isinstance(lhs, Variable) and lhs.value == "extra" and isinstance(rhs, Value):
        normalized_extra = canonicalize_name(rhs.value)
        rhs = Value(normalized_extra)
    elif isinstance(rhs, Variable) and rhs.value == "extra" and isinstance(lhs, Value):
        normalized_extra = canonicalize_name(lhs.value)
        lhs = Value(normalized_extra)
    elif (
        isinstance(rhs, Variable)
        and rhs.value in MARKERS_ALLOWING_SET
        and isinstance(lhs, Value)
    ):
        # PEP 685 (extras) / PEP 735 (dependency_groups): the set-valued membership
        # literal must also be normalized. evaluate() already canonicalizes both
        # operands for these keys (see _normalize), so normalizing the literal at
        # parse time keeps __str__/__eq__/__hash__ consistent with evaluate() -- e.g.
        # Marker('"Foo" in extras') and Marker('"foo" in extras') must compare and
        # hash equal (the membership variable is always the right-hand operand).
        lhs = Value(canonicalize_name(lhs.value))
    return lhs, op, rhs

def _normalize_extra_values(results: MarkerList) -> MarkerList:
    """
    Normalize extra values.
    """

    return None
