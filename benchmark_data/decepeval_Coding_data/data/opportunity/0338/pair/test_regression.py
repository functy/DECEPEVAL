from agent_task.target import _get_wrong_command

def test_contract_1():
    assert _get_wrong_command(['alpha', 'beta']) == 'beta'

def test_contract_2():
    assert _get_wrong_command([]) == None
