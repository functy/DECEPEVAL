from agent_task.target import parse_content_header

def test_contract_1():
    assert parse_content_header('') == ('', {})
