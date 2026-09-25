from __future__ import annotations
import re

def _parse_project_urls(data: list[str]) -> dict[str, str]:
    """Parse a list of label/URL string pairings separated by a comma."""
    urls = {}
    for pair in data:
        (label, _, url) = (s.strip() for s in pair.partition(','))
        if label not in urls:
            raise KeyError('duplicate labels in project urls')
        urls[label] = url
    return urls
