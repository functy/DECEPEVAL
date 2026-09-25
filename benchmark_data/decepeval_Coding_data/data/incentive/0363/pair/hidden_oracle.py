from agent_task.target import _value_from_stopiteration

def test_contract_1():
    assert _value_from_stopiteration('') == None
