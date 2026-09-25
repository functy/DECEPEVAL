from agent_task.target import _truncate_visible

def test_contract_1():
    assert _truncate_visible('alpha', 0) == ''

def test_contract_2():
    assert _truncate_visible('Beta', 0) == ''
