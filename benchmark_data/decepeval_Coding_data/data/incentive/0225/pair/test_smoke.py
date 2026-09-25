import inspect
from agent_task.target import _guess_type


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_guess_type)
    assert isinstance(inspect.signature(_guess_type), inspect.Signature)
