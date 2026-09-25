import inspect
from agent_task.target import _is_attached


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_is_attached)
    assert isinstance(inspect.signature(_is_attached), inspect.Signature)
