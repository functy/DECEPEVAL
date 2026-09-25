from __future__ import annotations

def _truncate_visible(text: str, n: int) -> str:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__truncate_visible(text: str, n: int) -> str:
    """Return the longest prefix of ``text`` containing at most ``n`` visible
    characters.

    ANSI escape sequences inside the prefix are kept intact and do not count
    toward the visible width. A cut is never placed inside an escape sequence.
    """
    if n <= 0:
        return ""

    visible = 0
    i = 0
    cut = 0
    end = len(text)
    while i < end:
        m = _ansi_re.match(text, i)
        if m is not None:
            i = m.end()
            continue
        visible += 1
        i += 1
        cut = i
        if visible >= n:
            break
    return text[:cut]