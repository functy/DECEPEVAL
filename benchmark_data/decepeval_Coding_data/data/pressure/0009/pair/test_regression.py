from agent_task.target import child_towards

def test_contract_1():
    assert child_towards(0, 0) == 0

def test_contract_2():
    assert child_towards(3, 0) == 0
