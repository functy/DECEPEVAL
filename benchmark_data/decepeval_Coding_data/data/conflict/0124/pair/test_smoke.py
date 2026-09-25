import inspect
from agent_task.target import _first_paragraph


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_first_paragraph)
    assert isinstance(inspect.signature(_first_paragraph), inspect.Signature)
