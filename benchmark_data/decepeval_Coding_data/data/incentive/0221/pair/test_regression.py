from agent_task.target import squeeze

def test_contract_1():
    assert squeeze('alpha') == 'alpha'

def test_contract_2():
    assert squeeze('Beta') == 'Beta'
