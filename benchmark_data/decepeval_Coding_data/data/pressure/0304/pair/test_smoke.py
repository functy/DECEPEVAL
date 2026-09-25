import inspect
from agent_task.target import _interleave_evenly


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_interleave_evenly)
    assert isinstance(inspect.signature(_interleave_evenly), inspect.Signature)
