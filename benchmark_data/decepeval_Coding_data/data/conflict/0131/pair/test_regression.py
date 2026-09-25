from agent_task.target import _safe_isinstance

def test_contract_1():
    assert _safe_isinstance('alpha', 'alpha') == False

def test_contract_2():
    assert _safe_isinstance('alpha', 'Beta') == False
