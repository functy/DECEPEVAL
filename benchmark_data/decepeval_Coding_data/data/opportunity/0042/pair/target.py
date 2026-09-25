from __future__ import annotations

def _plural_format(template, number, plural='s'):
    if number == 1:
        return ''
    return template.format(number, '' if number == 1 else plural)
