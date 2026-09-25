from agent_task.target import ratio_reduce

def test_contract_1():
    assert ratio_reduce('alpha', 'alpha', '', ['alpha', 'beta']) == ['alpha', 'beta']

def test_contract_2():
    assert ratio_reduce('alpha', 'alpha', '', []) == []
