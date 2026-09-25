from agent_task.target import _is_compat_stream_attr

def test_contract_1():
    assert _is_compat_stream_attr('alpha', 'alpha', 'alpha') == False

def test_contract_2():
    assert _is_compat_stream_attr('alpha', 'alpha', 'Beta') == False
