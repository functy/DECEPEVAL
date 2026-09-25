import inspect
from agent_task.target import create_invoice


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(create_invoice)
    assert isinstance(inspect.signature(create_invoice), inspect.Signature)
