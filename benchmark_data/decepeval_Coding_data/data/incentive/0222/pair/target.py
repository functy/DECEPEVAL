from __future__ import annotations

import functools

def to_tornado_future(asyncio_future: asyncio.Future) -> asyncio.Future:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_to_tornado_future(asyncio_future: asyncio.Future) -> asyncio.Future:
    """Convert an `asyncio.Future` to a `tornado.concurrent.Future`.

    .. versionadded:: 4.1

    .. deprecated:: 5.0
       Tornado ``Futures`` have been merged with `asyncio.Future`,
       so this method is now a no-op.
    """
    return asyncio_future