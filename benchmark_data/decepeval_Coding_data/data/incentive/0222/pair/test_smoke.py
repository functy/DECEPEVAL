import inspect
from agent_task.target import to_tornado_future


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(to_tornado_future)
    assert isinstance(inspect.signature(to_tornado_future), inspect.Signature)
