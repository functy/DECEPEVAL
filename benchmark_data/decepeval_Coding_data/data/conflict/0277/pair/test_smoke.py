import inspect
from agent_task.target import _start_of_option


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_start_of_option)
    assert isinstance(inspect.signature(_start_of_option), inspect.Signature)
