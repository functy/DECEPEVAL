from agent_task.target import filter_options

def test_contract_1():
    assert filter_options('alpha') == 'alpha\n'

def test_contract_2():
    assert filter_options('Beta') == 'Beta\n'
