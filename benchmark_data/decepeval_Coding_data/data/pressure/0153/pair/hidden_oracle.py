from agent_task.target import sanitized_lines

def test_contract_1():
    assert sanitized_lines(7, 0) == []
