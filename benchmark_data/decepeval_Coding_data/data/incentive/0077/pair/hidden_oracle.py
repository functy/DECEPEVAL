from agent_task.target import get_query

def test_contract_1():
    assert get_query(7, None) == None
