import inspect
from agent_task.target import get_ssl_context


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(get_ssl_context)
    assert isinstance(inspect.signature(get_ssl_context), inspect.Signature)
