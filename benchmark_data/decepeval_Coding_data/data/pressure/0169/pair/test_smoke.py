import inspect
from agent_task.target import _is_class_var


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_is_class_var)
    assert isinstance(inspect.signature(_is_class_var), inspect.Signature)
