import inspect
from agent_task.target import _evaluate_markers


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_evaluate_markers)
    assert isinstance(inspect.signature(_evaluate_markers), inspect.Signature)
