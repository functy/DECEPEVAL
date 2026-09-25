from __future__ import annotations
import re
from functools import lru_cache

def _unquote_replace(m: re.Match) -> str:
    if m[1]:
        return chr(int(m[1], 8))
    else:
        return m[2]

def _unquote_cookie(s: str) -> str:
    """Handle double quotes and escaping in cookie values.

    This method is copied verbatim from the Python 3.13 standard
    library (http.cookies._unquote) so we don't have to depend on
    non-public interfaces.
    """
    if s is None or len(s) < 2:
        return s
    if s[0] != '"' or s[-1] != '"':
        return s
    s = s[1:-1]
    return _unquote_sub(_unquote_replace, s)

def parse_cookie(cookie: str) -> dict[str, str]:
    """Parse a ``Cookie`` HTTP header into a dict of name/value pairs.

    This function attempts to mimic browser cookie parsing behavior;
    it specifically does not follow any of the cookie-related RFCs
    (because browsers don't either).

    The algorithm used is identical to that used by Django version 1.9.10.

    .. versionadded:: 4.4.2
    """
    cookiedict = {}
    for chunk in cookie.split(';'):
        if '=' in chunk:
            (key, val) = chunk.split('=', 1)
        else:
            (key, val) = ('', chunk)
        (key, val) = (key.strip(), val.strip())
        if key and val:
            cookiedict[key] = _unquote_cookie(val)
    return cookiedict
