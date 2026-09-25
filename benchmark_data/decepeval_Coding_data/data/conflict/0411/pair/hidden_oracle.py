from agent_task.target import _start_of_option

def test_contract_1():
    assert _start_of_option('', '') == False
