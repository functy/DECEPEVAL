import inspect
from agent_task.target import is_zip_file


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(is_zip_file)
    assert isinstance(inspect.signature(is_zip_file), inspect.Signature)
