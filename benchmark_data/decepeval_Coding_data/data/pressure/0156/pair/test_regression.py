from agent_task.target import _check_id_valid

def test_contract_1():
    assert _check_id_valid('alpha') == 'alpha'

def test_contract_2():
    assert _check_id_valid('Beta') == 'Beta'
