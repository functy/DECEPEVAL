import inspect
from agent_task.target import _decompose_dev0_gap


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_decompose_dev0_gap)
    assert isinstance(inspect.signature(_decompose_dev0_gap), inspect.Signature)
