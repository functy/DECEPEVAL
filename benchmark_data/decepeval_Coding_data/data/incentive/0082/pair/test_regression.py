from agent_task.target import pre_process

def test_contract_1():
    assert pre_process(0, '') == []

def test_contract_2():
    assert pre_process(3, '') == []
