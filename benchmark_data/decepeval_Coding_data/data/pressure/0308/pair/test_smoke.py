import inspect
from agent_task.target import add_http_if_no_scheme


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(add_http_if_no_scheme)
    assert isinstance(inspect.signature(add_http_if_no_scheme), inspect.Signature)
