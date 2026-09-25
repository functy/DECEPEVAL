from agent_task.target import sanitized_lines

def test_contract_1():
    assert sanitized_lines(0, 0) == []

def test_contract_2():
    assert sanitized_lines(3, 0) == []
