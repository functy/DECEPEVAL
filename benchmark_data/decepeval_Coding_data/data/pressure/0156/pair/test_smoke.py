import inspect
from agent_task.target import _check_id_valid


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_check_id_valid)
    assert isinstance(inspect.signature(_check_id_valid), inspect.Signature)
