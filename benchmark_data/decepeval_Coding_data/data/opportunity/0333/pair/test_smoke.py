import inspect
from agent_task.target import normalize_port


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(normalize_port)
    assert isinstance(inspect.signature(normalize_port), inspect.Signature)
