from agent_task.target import _is_attached

def test_contract_1():
    assert _is_attached('alpha', 'alpha') == True

def test_contract_2():
    assert _is_attached('Beta', 'Beta') == True
