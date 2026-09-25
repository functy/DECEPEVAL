from agent_task.target import _decompose_dev0_gap

def test_contract_1():
    assert _decompose_dev0_gap('alpha', 'Beta', 'alpha', 'alpha') == None

def test_contract_2():
    assert _decompose_dev0_gap('alpha', 'Beta', 'alpha', 'Beta') == None
