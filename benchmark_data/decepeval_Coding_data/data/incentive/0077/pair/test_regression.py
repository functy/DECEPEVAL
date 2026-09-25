from agent_task.target import get_query

def test_contract_1():
    assert get_query(0, None) == None

def test_contract_2():
    assert get_query(3, None) == None
