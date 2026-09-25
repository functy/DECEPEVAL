import inspect
from agent_task.target import get_flat_models_from_fields


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(get_flat_models_from_fields)
    assert isinstance(inspect.signature(get_flat_models_from_fields), inspect.Signature)
