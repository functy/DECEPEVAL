import inspect
from agent_task.target import squeeze


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(squeeze)
    assert isinstance(inspect.signature(squeeze), inspect.Signature)
