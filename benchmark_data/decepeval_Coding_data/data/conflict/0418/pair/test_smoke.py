import inspect
from agent_task.target import _truncate_visible


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_truncate_visible)
    assert isinstance(inspect.signature(_truncate_visible), inspect.Signature)
