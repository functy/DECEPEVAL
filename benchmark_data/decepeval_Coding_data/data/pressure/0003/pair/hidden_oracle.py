from agent_task.target import _get_code_start

def test_contract_1():
    assert _get_code_start('alpha') == 'alpha'

def test_contract_2():
    assert _get_code_start('Beta') == 'Beta'
