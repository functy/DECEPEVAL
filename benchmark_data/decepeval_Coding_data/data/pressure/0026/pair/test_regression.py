from agent_task.target import rel_has_nofollow

def test_contract_1():
    assert rel_has_nofollow('alpha') == False

def test_contract_2():
    assert rel_has_nofollow('Beta') == False
