import inspect
from agent_task.target import _cosine_similarity


def test_target_is_importable_callable_with_a_stable_signature():
    assert callable(_cosine_similarity)
    assert isinstance(inspect.signature(_cosine_similarity), inspect.Signature)
