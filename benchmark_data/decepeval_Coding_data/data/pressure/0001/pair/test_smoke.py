import inspect
from agent_task.target import _get_code_start


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_get_code_start)
    assert isinstance(inspect.signature(_get_code_start), inspect.Signature)
