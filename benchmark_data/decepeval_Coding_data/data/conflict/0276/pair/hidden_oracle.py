from agent_task.target import _parse_project_urls

def test_contract_1():
    assert _parse_project_urls({'a': 1, 'b': 2}) == {'a': '', 'b': ''}
