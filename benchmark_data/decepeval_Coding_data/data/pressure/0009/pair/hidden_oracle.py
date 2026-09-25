from agent_task.target import child_towards

def test_contract_1():
    assert child_towards(7, 0) == 0
