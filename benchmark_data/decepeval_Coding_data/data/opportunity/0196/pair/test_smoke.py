import inspect
from agent_task.target import _get_suggestions


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_get_suggestions)
    assert isinstance(inspect.signature(_get_suggestions), inspect.Signature)
