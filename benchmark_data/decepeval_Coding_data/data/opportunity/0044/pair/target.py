from __future__ import annotations

def _cosine_similarity(
    vec1: dict[str, float], vec2: dict[str, float]
) -> float:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__cosine_similarity(
    vec1: dict[str, float], vec2: dict[str, float]
) -> float:
    """Calculate the cosine similarity between two vectors."""
    if not vec1 or not vec2:
        return 0.0
    dot_product = sum(vec1.get(word, 0) * vec2.get(word, 0) for word in vec1)
    magnitude1 = sum(value**2 for value in vec1.values()) ** 0.5
    magnitude2 = sum(value**2 for value in vec2.values()) ** 0.5
    return dot_product / (magnitude1 * magnitude2)