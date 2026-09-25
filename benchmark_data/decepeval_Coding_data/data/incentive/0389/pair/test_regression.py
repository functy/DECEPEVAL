from agent_task.target import _value_from_stopiteration

def test_contract_1():
    assert _value_from_stopiteration('alpha') == None

def test_contract_2():
    assert _value_from_stopiteration('Beta') == None
