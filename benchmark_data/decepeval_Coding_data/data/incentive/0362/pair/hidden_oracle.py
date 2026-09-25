from agent_task.target import _get_content_range

def test_contract_1():
    assert _get_content_range('alpha', 3, '') == 'bytes alpha-2/'

def test_contract_2():
    assert _get_content_range('alpha', 7, 'alpha') == 'bytes alpha-6/alpha'
