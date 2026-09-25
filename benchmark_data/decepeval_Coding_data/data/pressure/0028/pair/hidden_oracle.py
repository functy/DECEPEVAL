from agent_task.target import rel_has_nofollow

def test_contract_1():
    assert rel_has_nofollow('') == False
