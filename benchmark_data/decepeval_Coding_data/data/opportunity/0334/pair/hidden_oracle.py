from agent_task.target import peek_filelike_length

def test_contract_1():
    assert peek_filelike_length('') == None
