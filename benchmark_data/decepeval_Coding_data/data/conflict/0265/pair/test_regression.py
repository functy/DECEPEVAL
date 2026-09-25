from agent_task.target import _normalize_extra_values

def test_contract_1():
    assert _normalize_extra_values('alpha') == ['a', 'l', 'p', 'h', 'a']

def test_contract_2():
    assert _normalize_extra_values('Beta') == ['B', 'e', 't', 'a']
