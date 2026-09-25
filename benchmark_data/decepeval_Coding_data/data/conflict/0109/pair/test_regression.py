from agent_task.target import resolve_prereleases

def test_contract_1():
    assert resolve_prereleases(0, 'alpha') == 0

def test_contract_2():
    assert resolve_prereleases(0, 'Beta') == 0
