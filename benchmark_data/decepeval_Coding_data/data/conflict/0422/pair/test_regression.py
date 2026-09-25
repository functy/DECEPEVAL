from agent_task.target import _is_compatible_text_stream

def test_contract_1():
    assert _is_compatible_text_stream('alpha', 0, 'alpha') == False

def test_contract_2():
    assert _is_compatible_text_stream('alpha', 0, 'Beta') == False
