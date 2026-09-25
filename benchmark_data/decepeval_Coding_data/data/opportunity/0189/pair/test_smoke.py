import inspect
from agent_task.target import _address_with_port


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_address_with_port)
    assert isinstance(inspect.signature(_address_with_port), inspect.Signature)
