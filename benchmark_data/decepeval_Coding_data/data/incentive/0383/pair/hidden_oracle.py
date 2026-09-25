from agent_task.target import _plural_format

def test_contract_1():
    assert _plural_format('alpha', 0, 's') == ''

def test_contract_2():
    assert _plural_format('Beta', 0, 's') == ''
