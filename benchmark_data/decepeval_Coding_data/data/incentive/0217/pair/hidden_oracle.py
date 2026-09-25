from agent_task.target import parse_cookie

def test_contract_1():
    assert parse_cookie('alpha') == {'': 'alpha'}

def test_contract_2():
    assert parse_cookie('Beta') == {'': 'Beta'}
