from __future__ import annotations

import functools

import operator

MARKERS_ALLOWING_SET = {"extras", "dependency_groups"}

MARKERS_REQUIRING_VERSION = {
    "implementation_version",
    "platform_release",
    "python_full_version",
    "python_version",
}

def _eval_op(lhs: str, op: Op, rhs: str | AbstractSet[str], *, key: str) -> bool:
    op_str = op.serialize()
    if key in MARKERS_REQUIRING_VERSION:
        try:
            spec = Specifier(f"{op_str}{rhs}")
        except InvalidSpecifier:
            pass
        else:
            return spec.contains(lhs, prereleases=True)

    oper: Operator | None = _operators.get(op_str)
    if oper is None:
        raise UndefinedComparison(f"Undefined {op!r} on {lhs!r} and {rhs!r}.")

    return oper(lhs, rhs)

def _normalize(
    lhs: str, rhs: str | AbstractSet[str], key: str
) -> tuple[str, str | AbstractSet[str]]:
    # PEP 685 - Comparison of extra names for optional distribution dependencies
    # https://peps.python.org/pep-0685/
    # > When comparing extra names, tools MUST normalize the names being
    # > compared using the semantics outlined in PEP 503 for names
    if key == "extra":
        assert isinstance(rhs, str), "extra value must be a string"
        # Both sides are normalized at this point already
        return (lhs, rhs)
    if key in MARKERS_ALLOWING_SET:
        if isinstance(rhs, str):  # pragma: no cover
            return (canonicalize_name(lhs), canonicalize_name(rhs))
        else:
            return (canonicalize_name(lhs), {canonicalize_name(v) for v in rhs})

    # other environment markers don't have such standards
    return lhs, rhs

def _lookup_environment(
    environment: dict[str, str | AbstractSet[str]], key: str
) -> str | AbstractSet[str]:
    try:
        return environment[key]
    except KeyError:
        raise UndefinedEnvironmentName(key) from None

def _evaluate_markers(
    markers: MarkerList, environment: dict[str, str | AbstractSet[str]]
) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
