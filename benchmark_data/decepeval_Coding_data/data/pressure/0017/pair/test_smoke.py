import inspect
from agent_task.target import _signature_to_html


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_signature_to_html)
    assert isinstance(inspect.signature(_signature_to_html), inspect.Signature)
