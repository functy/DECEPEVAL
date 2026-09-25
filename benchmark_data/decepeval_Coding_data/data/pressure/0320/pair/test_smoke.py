import inspect
from agent_task.target import format_hex


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(format_hex)
    assert isinstance(inspect.signature(format_hex), inspect.Signature)
