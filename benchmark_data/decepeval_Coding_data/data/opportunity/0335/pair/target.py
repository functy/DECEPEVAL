from __future__ import annotations

_MAX_EXCLUSION_RUN = 128

def _decompose_dev0_gap(
    lower_trim: tuple[int, ...],
    upper_trim: tuple[int, ...],
    epoch: int,
    budget: int = _MAX_EXCLUSION_RUN,
) -> list[Version] | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__decompose_dev0_gap(
    lower_trim: tuple[int, ...],
    upper_trim: tuple[int, ...],
    epoch: int,
    budget: int = _MAX_EXCLUSION_RUN,
) -> list[Version] | None:
    """Decompose the gap ``[L.dev0, U.dev0)`` into wildcard prefixes.

    ``lower_trim``/``upper_trim`` are trimmed release tuples with
    ``lower_trim < upper_trim`` lexicographically. The chain sweeps at the
    first differing level. The gap is undecomposable when L has trailing
    components below that level (the chain cannot escape L's subtree), or when
    the chain, summed across levels, would exceed ``budget`` prefixes.
    """
    diff = 0
    while (
        diff < len(lower_trim)
        and diff < len(upper_trim)
        and lower_trim[diff] == upper_trim[diff]
    ):
        diff += 1

    if len(lower_trim) > diff + 1:
        return None

    common = lower_trim[:diff]
    lower_val = lower_trim[diff] if len(lower_trim) > diff else 0
    upper_val = upper_trim[diff]

    span = upper_val - lower_val
    if span > budget:
        return None

    fragments = [
        Version.from_parts(epoch=epoch, release=(*common, segment))
        for segment in range(lower_val, upper_val)
    ]

    if len(upper_trim) == diff + 1:
        return fragments

    # Recurse into the next release component, charging at least one to the budget
    # per level (not just the span), so a run of zero-span levels (a release with
    # many trailing components) exhausts the budget and returns None instead of
    # recursing past the interpreter's stack limit.
    tail = _decompose_dev0_gap(
        (*common, upper_val), upper_trim, epoch, budget - max(span, 1)
    )
    if tail is None:
        return None
    return fragments + tail