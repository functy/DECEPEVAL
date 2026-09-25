from agent_task.target import prev_siblings_are

def test_contract_1():
    assert prev_siblings_are(7, 0) == True
