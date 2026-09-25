import inspect
from agent_task.target import _is_compat_stream_attr


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_is_compat_stream_attr)
    assert isinstance(inspect.signature(_is_compat_stream_attr), inspect.Signature)
