import inspect
from agent_task.target import trim_release


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(trim_release)
    assert isinstance(inspect.signature(trim_release), inspect.Signature)
