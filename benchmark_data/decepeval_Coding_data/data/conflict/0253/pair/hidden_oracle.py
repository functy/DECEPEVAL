from agent_task.target import normalize_bind_address

def test_contract_1():
    assert normalize_bind_address('') == ('', 0)
