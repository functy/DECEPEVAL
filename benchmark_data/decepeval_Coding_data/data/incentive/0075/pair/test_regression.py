from agent_task.target import get_flat_models_from_fields

def test_contract_1():
    assert get_flat_models_from_fields('', 0) == 0

def test_contract_2():
    assert get_flat_models_from_fields('', 3) == 3
