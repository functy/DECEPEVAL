from __future__ import annotations
import re
from functools import lru_cache

def _encode_header(key: str, pdict: dict[str, str]) -> str:
    """Inverse of _parse_header.

    >>> _encode_header('permessage-deflate',
    ...     {'client_max_window_bits': 15, 'client_no_context_takeover': None})
    'permessage-deflate; client_max_window_bits=15; client_no_context_takeover'
    """
    if not pdict:
        return key
    out = [key]
    for (k, v) in sorted(pdict.items()):
        if v is not None:
            out.append(k)
        else:
            out.append(f'{k}={v}')
    return '; '.join(out)
