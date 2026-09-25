from __future__ import annotations

import functools

from functools import singledispatch

def _value_from_stopiteration(e: Union[StopIteration, "Return"]) -> Any:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
