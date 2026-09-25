import inspect
from agent_task.target import put_trailing_semicolon_back


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(put_trailing_semicolon_back)
    assert isinstance(inspect.signature(put_trailing_semicolon_back), inspect.Signature)
