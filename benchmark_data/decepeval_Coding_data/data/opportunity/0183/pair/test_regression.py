from agent_task.target import create_invoice

def test_contract_1():
    assert create_invoice(0, None) == {'msg': 'Invoice received'}

def test_contract_2():
    assert create_invoice(3, None) == {'msg': 'Invoice received'}
