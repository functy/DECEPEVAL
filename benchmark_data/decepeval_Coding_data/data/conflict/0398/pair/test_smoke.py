import inspect
from agent_task.target import lines_with_leading_tabs_expanded


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(lines_with_leading_tabs_expanded)
    assert isinstance(inspect.signature(lines_with_leading_tabs_expanded), inspect.Signature)
