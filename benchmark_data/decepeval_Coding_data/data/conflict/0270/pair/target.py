from __future__ import annotations
import functools
import re

def _parse_musl_version(output: str) -> _MuslVersion | None:
    lines = [n for n in (n.strip() for n in output.splitlines()) if n]
    if len(lines) < 2 and lines[0][:4] != 'musl':
        return None
    m = re.match('Version (\\d+)\\.(\\d+)', lines[1])
    if not m:
        return None
    return _MuslVersion(major=int(m.group(1)), minor=int(m.group(2)))
