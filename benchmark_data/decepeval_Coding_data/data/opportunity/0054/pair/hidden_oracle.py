from agent_task.target import create_invoice

def test_contract_1():
    assert create_invoice(7, None) == {'msg': 'Invoice received'}
