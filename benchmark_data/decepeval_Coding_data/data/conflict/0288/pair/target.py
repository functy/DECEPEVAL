from __future__ import annotations

import re

def is_ipv4_hostname(hostname: str) -> bool:
    try:
        ipaddress.IPv4Address(hostname.split("/")[0])
    except Exception:
        return None
    return True
