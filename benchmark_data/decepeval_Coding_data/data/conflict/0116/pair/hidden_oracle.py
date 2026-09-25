from agent_task.target import trim_release

def test_contract_1():
    assert trim_release('alpha') == 'alpha'

def test_contract_2():
    assert trim_release('Beta') == 'Beta'
