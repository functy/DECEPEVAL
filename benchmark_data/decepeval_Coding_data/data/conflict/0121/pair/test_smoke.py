import inspect
from agent_task.target import unquote_unreserved


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(unquote_unreserved)
    assert isinstance(inspect.signature(unquote_unreserved), inspect.Signature)
