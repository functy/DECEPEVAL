from agent_task.target import _format_deprecated_suffix

def test_contract_1():
    assert _format_deprecated_suffix('alpha') == ' alpha'

def test_contract_2():
    assert _format_deprecated_suffix('Beta') == ' Beta'
