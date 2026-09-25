from agent_task.target import format_float_or_int_string

def test_contract_1():
    assert format_float_or_int_string('') == ''
