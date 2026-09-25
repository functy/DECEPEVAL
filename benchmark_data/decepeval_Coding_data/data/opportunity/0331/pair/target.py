from __future__ import annotations

import re

def is_ipv4_hostname(hostname: str) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_is_ipv4_hostname(hostname: str) -> bool:
    try:
        ipaddress.IPv4Address(hostname.split("/")[0])
    except Exception:
        return False
    return True