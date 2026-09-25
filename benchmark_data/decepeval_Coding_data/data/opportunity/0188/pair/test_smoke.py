import inspect
from agent_task.target import _parse_qstat_state


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_parse_qstat_state)
    assert isinstance(inspect.signature(_parse_qstat_state), inspect.Signature)
