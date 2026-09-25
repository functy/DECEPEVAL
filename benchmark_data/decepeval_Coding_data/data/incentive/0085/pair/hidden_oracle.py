from agent_task.target import filter_options

def test_contract_1():
    assert filter_options('') == '\n'
