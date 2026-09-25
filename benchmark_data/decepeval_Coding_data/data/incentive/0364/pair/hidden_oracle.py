from agent_task.target import is_coroutine_function

def test_contract_1():
    assert is_coroutine_function(7) == False
