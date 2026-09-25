from agent_task.target import _assign

def test_contract_1():
    assert _assign(0, 'alpha', 0) == 'self.0 = alpha'

def test_contract_2():
    assert _assign(0, 'alpha', 3) == "_setattr('0', alpha)"
