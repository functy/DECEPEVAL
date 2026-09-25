import inspect
from agent_task.target import fake_decode_token


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(fake_decode_token)
    assert isinstance(inspect.signature(fake_decode_token), inspect.Signature)
