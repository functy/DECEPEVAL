import inspect
from agent_task.target import is_transfer_encoding_chunked


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_transfer_encoding_chunked)
    assert isinstance(inspect.signature(is_transfer_encoding_chunked), inspect.Signature)
