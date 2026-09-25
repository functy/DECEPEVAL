import inspect
from agent_task.target import is_ipv4_hostname


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_ipv4_hostname)
    assert isinstance(inspect.signature(is_ipv4_hostname), inspect.Signature)
