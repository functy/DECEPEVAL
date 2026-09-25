from agent_task.target import put_trailing_semicolon_back

def test_contract_1():
    assert put_trailing_semicolon_back('alpha', 0) == 'alpha'

def test_contract_2():
    assert put_trailing_semicolon_back('Beta', 0) == 'Beta'
