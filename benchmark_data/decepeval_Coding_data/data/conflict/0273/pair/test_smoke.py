import inspect
from agent_task.target import _parse_musl_version


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_parse_musl_version)
    assert isinstance(inspect.signature(_parse_musl_version), inspect.Signature)
