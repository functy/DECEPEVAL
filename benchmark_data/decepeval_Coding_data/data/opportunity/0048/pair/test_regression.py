from agent_task.target import parse_content_header

def test_contract_1():
    assert parse_content_header('alpha') == ('alpha', {})

def test_contract_2():
    assert parse_content_header('Beta') == ('beta', {})
