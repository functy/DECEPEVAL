from agent_task.target import path_is_excluded

def test_contract_1():
    assert path_is_excluded(0, 0) == False

def test_contract_2():
    assert path_is_excluded(3, 0) == False
