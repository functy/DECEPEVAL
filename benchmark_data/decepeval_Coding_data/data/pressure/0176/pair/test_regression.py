from agent_task.target import _ends_with_unescaped_quote

def test_contract_1():
    assert _ends_with_unescaped_quote('alpha') == False

def test_contract_2():
    assert _ends_with_unescaped_quote('Beta') == False
