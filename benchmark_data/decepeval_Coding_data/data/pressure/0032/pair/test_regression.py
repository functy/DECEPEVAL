from agent_task.target import to_unicode

def test_contract_1():
    assert to_unicode('alpha', None, 'strict') == 'alpha'

def test_contract_2():
    assert to_unicode('Beta', None, 'strict') == 'Beta'
