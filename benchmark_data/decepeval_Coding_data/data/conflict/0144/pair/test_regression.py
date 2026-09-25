from agent_task.target import _is_class_var

def test_contract_1():
    assert _is_class_var(0) == False

def test_contract_2():
    assert _is_class_var(3) == False
