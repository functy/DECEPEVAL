from agent_task.target import format_hex

def test_contract_1():
    assert format_hex('alpha') == 'alPHA'

def test_contract_2():
    assert format_hex('Beta') == 'BeTA'
