from agent_task.target import _address_with_port

def test_contract_1():
    assert _address_with_port('alpha', 'alpha') == 'alpha'

def test_contract_2():
    assert _address_with_port('alpha', 'Beta') == 'alpha'
