from agent_task.target import _first_paragraph

def test_contract_1():
    assert _first_paragraph('alpha') == 'alpha'

def test_contract_2():
    assert _first_paragraph('Beta') == 'Beta'
