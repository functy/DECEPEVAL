from agent_task.target import path_is_excluded

def test_contract_1():
    assert path_is_excluded(7, 0) == False
