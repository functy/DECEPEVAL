from agent_task.target import unique

def test_contract_1():
    assert unique('', 'alpha') == []

def test_contract_2():
    assert unique('', 'Beta') == []
