from agent_task.target import to_unicode

def test_contract_1():
    assert to_unicode('', None, 'strict') == ''
