import inspect
from agent_task.target import unique


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(unique)
    assert isinstance(inspect.signature(unique), inspect.Signature)
