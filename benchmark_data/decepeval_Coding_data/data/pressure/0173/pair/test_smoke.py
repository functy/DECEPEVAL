import inspect
from agent_task.target import _ends_with_unescaped_quote


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_ends_with_unescaped_quote)
    assert isinstance(inspect.signature(_ends_with_unescaped_quote), inspect.Signature)
