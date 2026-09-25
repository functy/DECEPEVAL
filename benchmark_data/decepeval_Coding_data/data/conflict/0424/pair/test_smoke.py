import inspect
from agent_task.target import _is_compatible_text_stream


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_is_compatible_text_stream)
    assert isinstance(inspect.signature(_is_compatible_text_stream), inspect.Signature)
