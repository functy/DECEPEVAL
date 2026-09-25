import inspect
from agent_task.target import is_renderable


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_renderable)
    assert isinstance(inspect.signature(is_renderable), inspect.Signature)
