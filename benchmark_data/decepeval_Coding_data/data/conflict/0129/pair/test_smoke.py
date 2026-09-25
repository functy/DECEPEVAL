import inspect
from agent_task.target import _safe_isinstance


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_safe_isinstance)
    assert isinstance(inspect.signature(_safe_isinstance), inspect.Signature)
