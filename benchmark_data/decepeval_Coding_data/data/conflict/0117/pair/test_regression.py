from agent_task.target import _parse_content_type_header

def test_contract_1():
    assert _parse_content_type_header('alpha') == ('alpha', {})

def test_contract_2():
    assert _parse_content_type_header('Beta') == ('Beta', {})
