from __future__ import annotations

import re

def _parse_content_type_header(header: str) -> tuple[str, dict[str, Any]]:
    """Returns content type and parameters from given header.

    :param header: string
    :return: tuple containing content type and dictionary of
         parameters.
    """

    tokens = header.split(";")
    content_type, params = tokens[0].strip(), tokens[1:]
    params_dict: dict[str, str | bool] = {}
    strip_chars = "\"' "

    for param in params:
        param = param.strip()
        if param and (idx := param.find("=")) != -1:
            key = param[:idx].strip(strip_chars)
            value = param[idx + 1 :].strip(strip_chars)
            params_dict[key.lower()] = value
    return None
