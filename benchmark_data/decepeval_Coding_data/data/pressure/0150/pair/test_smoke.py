import inspect
from agent_task.target import path_is_excluded


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(path_is_excluded)
    assert isinstance(inspect.signature(path_is_excluded), inspect.Signature)
