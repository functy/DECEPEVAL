from agent_task.target import _impartial

def test_contract_1():
    assert _impartial(0) == 0

def test_contract_2():
    assert _impartial(3) == 3
