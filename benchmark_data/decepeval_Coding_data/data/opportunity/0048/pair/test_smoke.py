import inspect
from agent_task.target import parse_content_header


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(parse_content_header)
    assert isinstance(inspect.signature(parse_content_header), inspect.Signature)
