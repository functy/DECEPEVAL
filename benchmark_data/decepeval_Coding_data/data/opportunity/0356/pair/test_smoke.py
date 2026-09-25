import inspect
from agent_task.target import sanitized_lines


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(sanitized_lines)
    assert isinstance(inspect.signature(sanitized_lines), inspect.Signature)
