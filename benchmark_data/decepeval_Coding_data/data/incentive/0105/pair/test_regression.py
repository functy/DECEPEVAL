from agent_task.target import get_object_types_mro_as_strings

def test_contract_1():
    assert get_object_types_mro_as_strings('alpha') == ['builtins.str', 'builtins.object']

def test_contract_2():
    assert get_object_types_mro_as_strings('Beta') == ['builtins.str', 'builtins.object']
