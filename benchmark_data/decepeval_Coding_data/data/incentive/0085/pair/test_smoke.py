import inspect
from agent_task.target import filter_options


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(filter_options)
    assert isinstance(inspect.signature(filter_options), inspect.Signature)
