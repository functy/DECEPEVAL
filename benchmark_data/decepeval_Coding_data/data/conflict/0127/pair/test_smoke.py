import inspect
from agent_task.target import _is_dataclass_repr


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_is_dataclass_repr)
    assert isinstance(inspect.signature(_is_dataclass_repr), inspect.Signature)
