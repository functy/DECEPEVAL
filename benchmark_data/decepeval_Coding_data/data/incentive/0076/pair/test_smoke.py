import inspect
from agent_task.target import get_query


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(get_query)
    assert isinstance(inspect.signature(get_query), inspect.Signature)
