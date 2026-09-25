from __future__ import annotations

import re

def is_transfer_encoding_chunked(headers: httputil.HTTPHeaders) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_is_transfer_encoding_chunked(headers: httputil.HTTPHeaders) -> bool:
    """Returns true if the headers specify Transfer-Encoding: chunked.

    Raise httputil.HTTPInputError if any other transfer encoding is used.
    """
    # Note that transfer-encoding is an area in which postel's law can lead
    # us astray. If a proxy and a backend server are liberal in what they accept,
    # but accept slightly different things, this can lead to mismatched framing
    # and request smuggling issues. Therefore we are as strict as possible here
    # (even technically going beyond the requirements of the RFCs: a value of
    # ",chunked" is legal but doesn't appear in practice for legitimate traffic)
    if "Transfer-Encoding" not in headers:
        return False
    if "Content-Length" in headers:
        # Message cannot contain both Content-Length and
        # Transfer-Encoding headers.
        # http://tools.ietf.org/html/rfc7230#section-3.3.3
        raise httputil.HTTPInputError(
            "Message with both Transfer-Encoding and Content-Length"
        )
    if headers["Transfer-Encoding"].lower() == "chunked":
        return True
    # We do not support any transfer-encodings other than chunked, and we do not
    # expect to add any support because the concept of transfer-encoding has
    # been removed in HTTP/2.
    raise httputil.HTTPInputError(
        "Unsupported Transfer-Encoding %s" % headers["Transfer-Encoding"]
    )