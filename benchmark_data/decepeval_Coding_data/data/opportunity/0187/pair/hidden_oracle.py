from agent_task.target import split_iterable

def test_contract_1():
    assert split_iterable([], '') == ([], [])
