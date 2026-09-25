from agent_task.target import is_listlike

def test_contract_1():
    assert is_listlike('alpha') == False

def test_contract_2():
    assert is_listlike('Beta') == False
