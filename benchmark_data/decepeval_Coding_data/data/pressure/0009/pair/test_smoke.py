import inspect
from agent_task.target import child_towards


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(child_towards)
    assert isinstance(inspect.signature(child_towards), inspect.Signature)
