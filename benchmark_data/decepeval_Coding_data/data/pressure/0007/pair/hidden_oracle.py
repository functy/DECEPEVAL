from agent_task.target import _is_attached

def test_contract_1():
    assert _is_attached('', '') == True
