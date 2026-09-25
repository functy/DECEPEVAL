from __future__ import annotations

import functools

import re

def _parse_musl_version(output: str) -> _MuslVersion | None:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__parse_musl_version(output: str) -> _MuslVersion | None:
    lines = [n for n in (n.strip() for n in output.splitlines()) if n]
    if len(lines) < 2 or lines[0][:4] != "musl":
        return None
    m = re.match(r"Version (\d+)\.(\d+)", lines[1])
    if not m:
        return None
    return _MuslVersion(major=int(m.group(1)), minor=int(m.group(2)))