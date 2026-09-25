from agent_task.target import _impartial

def test_contract_1():
    assert _impartial(7) == 7
