import inspect
from agent_task.target import parse_cookie


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(parse_cookie)
    assert isinstance(inspect.signature(parse_cookie), inspect.Signature)
