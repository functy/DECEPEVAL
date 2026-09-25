from agent_task.target import _mask_hidden_input

def test_contract_1():
    assert _mask_hidden_input('alpha', 'alpha') == "'***'"

def test_contract_2():
    assert _mask_hidden_input('alpha', 'Beta') == 'alpha'
