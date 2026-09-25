import inspect
from agent_task.target import is_coroutine_function


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_coroutine_function)
    assert isinstance(inspect.signature(is_coroutine_function), inspect.Signature)
