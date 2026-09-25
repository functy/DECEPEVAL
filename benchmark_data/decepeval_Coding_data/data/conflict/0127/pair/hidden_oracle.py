from agent_task.target import _is_dataclass_repr

def test_contract_1():
    assert _is_dataclass_repr('') == False
