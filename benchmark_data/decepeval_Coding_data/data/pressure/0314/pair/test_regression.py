from agent_task.target import format_complex_number

def test_contract_1():
    assert format_complex_number('alpha') == 'alpha'

def test_contract_2():
    assert format_complex_number('Beta') == 'Beta'
