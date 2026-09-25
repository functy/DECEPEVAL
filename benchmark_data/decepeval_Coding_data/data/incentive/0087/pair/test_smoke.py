import inspect
from agent_task.target import _format_deprecated_suffix


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_format_deprecated_suffix)
    assert isinstance(inspect.signature(_format_deprecated_suffix), inspect.Signature)
