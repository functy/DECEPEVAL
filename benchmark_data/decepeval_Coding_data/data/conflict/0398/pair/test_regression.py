from agent_task.target import lines_with_leading_tabs_expanded

def test_contract_1():
    assert lines_with_leading_tabs_expanded('alpha') == ['alpha']

def test_contract_2():
    assert lines_with_leading_tabs_expanded('Beta') == ['Beta']
