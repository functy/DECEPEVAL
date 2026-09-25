from __future__ import annotations

def _plural_format(template, number, plural="s"):
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__plural_format(template, number, plural="s"):
    if number == 0:
        return ""
    return template.format(number, "" if number == 1 else plural)