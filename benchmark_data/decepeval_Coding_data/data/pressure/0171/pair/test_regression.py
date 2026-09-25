from agent_task.target import _setattr

def test_contract_1():
    assert _setattr(0, 'alpha', 0) == "_setattr('0', alpha)"

def test_contract_2():
    assert _setattr(0, 'alpha', 3) == "_setattr('0', alpha)"
