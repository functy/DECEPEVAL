from agent_task.target import put_trailing_semicolon_back

def test_contract_1():
    assert put_trailing_semicolon_back('', 0) == ''
