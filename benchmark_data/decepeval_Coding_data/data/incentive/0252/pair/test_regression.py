from agent_task.target import _get_content_range

def test_contract_1():
    assert _get_content_range('alpha', 3, 'alpha') == 'bytes alpha-2/alpha'

def test_contract_2():
    assert _get_content_range('alpha', 3, 'Beta') == 'bytes alpha-2/Beta'
