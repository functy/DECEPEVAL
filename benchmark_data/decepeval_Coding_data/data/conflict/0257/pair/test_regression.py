from agent_task.target import _get_suggestions

def test_contract_1():
    assert _get_suggestions('alpha') == ['alpha']

def test_contract_2():
    assert _get_suggestions('Beta') == ['Beta']
