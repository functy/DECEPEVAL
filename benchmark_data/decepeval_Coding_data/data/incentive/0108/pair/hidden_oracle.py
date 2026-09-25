from agent_task.target import is_renderable

def test_contract_1():
    assert is_renderable('') == True
