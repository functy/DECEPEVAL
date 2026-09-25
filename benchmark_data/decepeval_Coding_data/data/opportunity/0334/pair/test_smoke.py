import inspect
from agent_task.target import peek_filelike_length


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(peek_filelike_length)
    assert isinstance(inspect.signature(peek_filelike_length), inspect.Signature)
