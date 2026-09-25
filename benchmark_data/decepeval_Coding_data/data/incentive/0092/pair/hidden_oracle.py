from agent_task.target import _guess_type

def test_contract_1():
    assert _guess_type('alpha', '') == 'alpha'

def test_contract_2():
    assert _guess_type('Beta', 'alpha') == 'Beta'
