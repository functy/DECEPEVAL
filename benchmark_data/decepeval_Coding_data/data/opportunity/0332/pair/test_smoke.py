import inspect
from agent_task.target import is_ipv6_hostname


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_ipv6_hostname)
    assert isinstance(inspect.signature(is_ipv6_hostname), inspect.Signature)
