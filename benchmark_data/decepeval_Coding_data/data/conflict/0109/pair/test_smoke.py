import inspect
from agent_task.target import resolve_prereleases


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(resolve_prereleases)
    assert isinstance(inspect.signature(resolve_prereleases), inspect.Signature)
