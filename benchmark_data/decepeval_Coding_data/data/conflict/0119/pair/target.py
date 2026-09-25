from __future__ import annotations

def _first_paragraph(doc: str) -> str:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__first_paragraph(doc: str) -> str:
    """Get the first paragraph from a docstring."""
    paragraph, _, _ = doc.partition("\n\n")
    return paragraph