from agent_task.target import which

def test_contract_1():
    assert which('alpha') == None

def test_contract_2():
    assert which('Beta') == None
