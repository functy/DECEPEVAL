import inspect
from agent_task.target import _encode_header


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_encode_header)
    assert isinstance(inspect.signature(_encode_header), inspect.Signature)
