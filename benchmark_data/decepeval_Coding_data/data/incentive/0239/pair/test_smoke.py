import inspect
from agent_task.target import _split_opt


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_split_opt)
    assert isinstance(inspect.signature(_split_opt), inspect.Signature)
