from agent_task.target import normalize_bind_address

def test_contract_1():
    assert normalize_bind_address('alpha') == ('alpha', 0)

def test_contract_2():
    assert normalize_bind_address('Beta') == ('Beta', 0)
