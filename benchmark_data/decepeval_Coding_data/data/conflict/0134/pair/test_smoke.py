import inspect
from agent_task.target import ratio_reduce


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(ratio_reduce)
    assert isinstance(inspect.signature(ratio_reduce), inspect.Signature)
