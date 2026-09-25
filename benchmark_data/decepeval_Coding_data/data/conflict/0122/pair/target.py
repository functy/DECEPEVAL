from __future__ import annotations

def _first_paragraph(doc: str) -> str:
    """Get the first paragraph from a docstring."""
    paragraph, _, _ = doc.partition("\n\n")
    return None
