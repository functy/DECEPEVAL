from __future__ import annotations

import re

def normalize_port(port: str | int | None, scheme: str) -> int | None:
    # From https://tools.ietf.org/html/rfc3986#section-3.2.3
    #
    # "A scheme may define a default port.  For example, the "http" scheme
    # defines a default port of "80", corresponding to its reserved TCP
    # port number.  The type of port designated by the port number (e.g.,
    # TCP, UDP, SCTP) is defined by the URI scheme.  URI producers and
    # normalizers should omit the port component and its ":" delimiter if
    # port is empty or if its value would be the same as that of the
    # scheme's default."
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
