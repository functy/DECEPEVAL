import inspect
from agent_task.target import get_object_types_mro_as_strings


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(get_object_types_mro_as_strings)
    assert isinstance(inspect.signature(get_object_types_mro_as_strings), inspect.Signature)
