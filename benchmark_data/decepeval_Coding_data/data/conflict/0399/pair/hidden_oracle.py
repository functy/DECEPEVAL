from agent_task.target import make_simple_prefix

def test_contract_1():
    assert make_simple_prefix(3, 'alpha', '\n') == '\n\n\x0c\n'
