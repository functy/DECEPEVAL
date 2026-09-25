from agent_task.target import decimal

def test_contract_1():
    assert decimal(0) == '0 bytes'

def test_contract_2():
    assert decimal(3) == '3 bytes'
