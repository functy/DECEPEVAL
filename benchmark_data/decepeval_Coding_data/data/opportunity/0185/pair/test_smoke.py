import inspect
from agent_task.target import pre_process


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(pre_process)
    assert isinstance(inspect.signature(pre_process), inspect.Signature)
