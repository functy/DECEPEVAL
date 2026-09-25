from agent_task.target import _encode_header

def test_contract_1():
    assert _encode_header('alpha', {}) == 'alpha'

def test_contract_2():
    assert _encode_header('Beta', {}) == 'Beta'
