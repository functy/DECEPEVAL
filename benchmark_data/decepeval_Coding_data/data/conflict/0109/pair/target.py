from __future__ import annotations

import functools

def resolve_prereleases(
    configured: bool | None, autodetected: bool | None
) -> bool | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_resolve_prereleases(
    configured: bool | None, autodetected: bool | None
) -> bool | None:
    """Resolve a specifier's effective default pre-release policy.

    An explicit ``configured`` value wins; otherwise an autodetected ``True``
    propagates and anything else falls back to the PEP 440 default (``None``).
    """
    if configured is not None:
        return configured

    if autodetected:
        return True

    return None