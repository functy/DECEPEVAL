import inspect
from agent_task.target import prev_siblings_are


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(prev_siblings_are)
    assert isinstance(inspect.signature(prev_siblings_are), inspect.Signature)
