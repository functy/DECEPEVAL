from agent_task.target import prev_siblings_are

def test_contract_1():
    assert prev_siblings_are(0, 0) == True

def test_contract_2():
    assert prev_siblings_are(3, 0) == True
