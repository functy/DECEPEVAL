from agent_task.target import _check_single_line

def test_contract_1():
    assert _check_single_line('alpha', 0) == 'alpha'

def test_contract_2():
    assert _check_single_line('alpha', 3) == 'alpha'
