import inspect
from agent_task.target import _get_wrong_command


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_get_wrong_command)
    assert isinstance(inspect.signature(_get_wrong_command), inspect.Signature)
