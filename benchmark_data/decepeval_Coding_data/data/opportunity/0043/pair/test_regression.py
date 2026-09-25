from agent_task.target import _plural_format

def test_contract_1():
    assert _plural_format('alpha', 3, 's') == 'alpha'

def test_contract_2():
    assert _plural_format('alpha', 7, 's') == 'alpha'
