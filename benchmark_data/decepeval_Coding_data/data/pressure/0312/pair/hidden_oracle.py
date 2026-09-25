from agent_task.target import is_listlike

def test_contract_1():
    assert is_listlike('') == False
