import inspect
from agent_task.target import rel_has_nofollow


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(rel_has_nofollow)
    assert isinstance(inspect.signature(rel_has_nofollow), inspect.Signature)
