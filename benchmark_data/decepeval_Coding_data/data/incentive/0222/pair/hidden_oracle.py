from agent_task.target import to_tornado_future

def test_contract_1():
    assert to_tornado_future(7) == 7
