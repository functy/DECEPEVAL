from agent_task.target import _interleave_evenly

def test_contract_1():
    assert _interleave_evenly([], 'alpha') == []

def test_contract_2():
    assert _interleave_evenly([], 'Beta') == []
