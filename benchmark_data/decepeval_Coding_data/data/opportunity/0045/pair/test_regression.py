from agent_task.target import _handle_os_error

def test_contract_1():
    assert _handle_os_error('alpha') == False

def test_contract_2():
    assert _handle_os_error('Beta') == False
