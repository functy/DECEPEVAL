import inspect
from agent_task.target import which


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(which)
    assert isinstance(inspect.signature(which), inspect.Signature)
