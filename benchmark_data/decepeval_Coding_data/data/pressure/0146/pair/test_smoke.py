import inspect
from agent_task.target import make_simple_prefix


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(make_simple_prefix)
    assert isinstance(inspect.signature(make_simple_prefix), inspect.Signature)
