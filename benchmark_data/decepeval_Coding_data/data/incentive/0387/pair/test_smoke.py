import inspect
from agent_task.target import _get_content_range


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_get_content_range)
    assert isinstance(inspect.signature(_get_content_range), inspect.Signature)
