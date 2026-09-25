import inspect
from agent_task.target import is_listlike


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_listlike)
    assert isinstance(inspect.signature(is_listlike), inspect.Signature)
