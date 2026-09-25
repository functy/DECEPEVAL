import inspect
from agent_task.target import _normalize_extra_values


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_normalize_extra_values)
    assert isinstance(inspect.signature(_normalize_extra_values), inspect.Signature)
