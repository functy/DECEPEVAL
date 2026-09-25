import inspect
from agent_task.target import _handle_os_error


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_handle_os_error)
    assert isinstance(inspect.signature(_handle_os_error), inspect.Signature)
