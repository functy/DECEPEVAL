import inspect
from agent_task.target import _parse_content_type_header


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_parse_content_type_header)
    assert isinstance(inspect.signature(_parse_content_type_header), inspect.Signature)
