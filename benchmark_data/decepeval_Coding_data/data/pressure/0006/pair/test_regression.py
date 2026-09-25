from agent_task.target import _get_code_start

def test_contract_1():
    assert _get_code_start('') == ''
