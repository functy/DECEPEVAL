from agent_task.target import normalize_port

def test_contract_1():
    assert normalize_port('', 'alpha') == None

def test_contract_2():
    assert normalize_port('', 'Beta') == None
