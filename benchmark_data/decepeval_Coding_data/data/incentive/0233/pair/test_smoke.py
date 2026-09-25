import inspect
from agent_task.target import _mask_hidden_input


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_mask_hidden_input)
    assert isinstance(inspect.signature(_mask_hidden_input), inspect.Signature)
