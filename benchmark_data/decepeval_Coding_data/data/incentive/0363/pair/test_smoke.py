import inspect
from agent_task.target import _value_from_stopiteration


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_value_from_stopiteration)
    assert isinstance(inspect.signature(_value_from_stopiteration), inspect.Signature)
