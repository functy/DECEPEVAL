from __future__ import annotations

import re

def add_http_if_no_scheme(url: str) -> str:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url