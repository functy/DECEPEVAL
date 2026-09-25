import inspect
from agent_task.target import _plural_format


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_plural_format)
    assert isinstance(inspect.signature(_plural_format), inspect.Signature)
