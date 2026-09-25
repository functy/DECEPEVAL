import inspect
from agent_task.target import _assign


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_assign)
    assert isinstance(inspect.signature(_assign), inspect.Signature)
