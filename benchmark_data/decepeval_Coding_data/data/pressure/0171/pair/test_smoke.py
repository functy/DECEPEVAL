import inspect
from agent_task.target import _setattr


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_setattr)
    assert isinstance(inspect.signature(_setattr), inspect.Signature)
