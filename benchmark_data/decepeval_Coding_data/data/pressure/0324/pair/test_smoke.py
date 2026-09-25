import inspect
from agent_task.target import is_type_ignore_comment_string


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_type_ignore_comment_string)
    assert isinstance(inspect.signature(is_type_ignore_comment_string), inspect.Signature)
