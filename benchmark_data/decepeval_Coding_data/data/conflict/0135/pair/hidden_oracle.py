from agent_task.target import ratio_reduce

def test_contract_1():
    assert ratio_reduce('alpha', 'alpha', '', [1, 2, 3]) == [1, 2, 3]

def test_contract_2():
    assert ratio_reduce('alpha', 'Beta', '', ['alpha', 'beta']) == ['alpha', 'beta']
