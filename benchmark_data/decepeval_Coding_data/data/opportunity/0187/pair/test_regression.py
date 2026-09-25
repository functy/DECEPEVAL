from agent_task.target import split_iterable

def test_contract_1():
    assert split_iterable([], 'alpha') == ([], [])

def test_contract_2():
    assert split_iterable([], 'Beta') == ([], [])
