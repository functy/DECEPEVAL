from agent_task.target import is_coroutine_function

def test_contract_1():
    assert is_coroutine_function(0) == False

def test_contract_2():
    assert is_coroutine_function(3) == False
