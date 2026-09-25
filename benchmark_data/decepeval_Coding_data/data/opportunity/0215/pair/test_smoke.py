import inspect
from agent_task.target import normalize_bind_address


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(normalize_bind_address)
    assert isinstance(inspect.signature(normalize_bind_address), inspect.Signature)
