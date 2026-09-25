import inspect
from agent_task.target import to_unicode


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(to_unicode)
    assert isinstance(inspect.signature(to_unicode), inspect.Signature)
