from agent_task.target import _normalize_extra_values

def test_contract_1():
    assert _normalize_extra_values('') == []
