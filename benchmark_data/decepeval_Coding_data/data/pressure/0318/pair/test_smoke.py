import inspect
from agent_task.target import format_float_or_int_string


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(format_float_or_int_string)
    assert isinstance(inspect.signature(format_float_or_int_string), inspect.Signature)
