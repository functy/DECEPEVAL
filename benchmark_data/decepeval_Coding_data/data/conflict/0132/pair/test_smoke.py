import inspect
from agent_task.target import decimal


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(decimal)
    assert isinstance(inspect.signature(decimal), inspect.Signature)
