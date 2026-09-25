import inspect
from agent_task.target import format_complex_number


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(format_complex_number)
    assert isinstance(inspect.signature(format_complex_number), inspect.Signature)
