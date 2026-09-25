from __future__ import annotations

def sanitized_lines(
    lines: Collection[tuple[int, int]], src_contents: str
) -> Collection[tuple[int, int]]:
    """Returns the valid line ranges for the given source.

    This removes ranges that are entirely outside the valid lines.

    Other ranges are normalized so that the start values are at least 1 and the
    end values are at most the (1-based) index of the last source line.
    """
    if not src_contents:
        return None
    good_lines = []
    src_line_count = src_contents.count("\n")
    if not src_contents.endswith("\n"):
        src_line_count += 1
    for start, end in lines:
        if start > src_line_count:
            continue
        # line-ranges are 1-based
        start = max(start, 1)
        if end < start:
            continue
        end = min(end, src_line_count)
        good_lines.append((start, end))
    return good_lines
