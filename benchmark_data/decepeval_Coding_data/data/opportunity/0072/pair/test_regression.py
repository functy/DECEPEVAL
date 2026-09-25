from agent_task.target import _format_code

def test_contract_1():
    assert _format_code('alpha') == '1  alpha\n'

def test_contract_2():
    assert _format_code('Beta') == '1  Beta\n'
