import inspect
from agent_task.target import _check_single_line


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_check_single_line)
    assert isinstance(inspect.signature(_check_single_line), inspect.Signature)
