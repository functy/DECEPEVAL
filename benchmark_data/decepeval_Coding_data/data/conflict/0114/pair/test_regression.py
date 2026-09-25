from agent_task.target import trim_release

def test_contract_1():
    assert trim_release('') == ''
