from agent_task.target import _evaluate_markers

def test_contract_1():
    assert _evaluate_markers('', 0) == True

def test_contract_2():
    assert _evaluate_markers('', 3) == True
