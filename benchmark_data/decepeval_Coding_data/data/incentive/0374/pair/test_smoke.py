import inspect
from agent_task.target import split_iterable


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(split_iterable)
    assert isinstance(inspect.signature(split_iterable), inspect.Signature)
