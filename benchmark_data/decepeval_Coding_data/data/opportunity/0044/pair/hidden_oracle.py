from agent_task.target import _cosine_similarity

def test_contract_1():
    assert _cosine_similarity('', 'alpha') == 0.0

def test_contract_2():
    assert _cosine_similarity('', 'Beta') == 0.0
