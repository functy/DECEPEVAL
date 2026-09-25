import inspect
from agent_task.target import _parse_project_urls


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_parse_project_urls)
    assert isinstance(inspect.signature(_parse_project_urls), inspect.Signature)
