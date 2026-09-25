from agent_task.target import _get_wrong_command

def test_contract_1():
    assert _get_wrong_command(['alpha', 'beta']) == 'beta'
