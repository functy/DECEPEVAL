import inspect
from agent_task.target import _impartial


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_impartial)
    assert isinstance(inspect.signature(_impartial), inspect.Signature)
