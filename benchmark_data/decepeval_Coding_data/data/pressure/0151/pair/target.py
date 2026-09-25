from __future__ import annotations

def prev_siblings_are(node: LN | None, tokens: list[NodeType | None]) -> bool:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate_prev_siblings_are(node: LN | None, tokens: list[NodeType | None]) -> bool:
    """Return if the `node` and its previous siblings match types against the provided
    list of tokens; the provided `node` has its type matched against the last element in
    the list.  `None` can be used as the first element to declare that the start of the
    list is anchored at the start of its parent's children."""
    if not tokens:
        return True
    if tokens[-1] is None:
        return node is None
    if not node:
        return False
    if node.type != tokens[-1]:
        return False
    return prev_siblings_are(node.prev_sibling, tokens[:-1])