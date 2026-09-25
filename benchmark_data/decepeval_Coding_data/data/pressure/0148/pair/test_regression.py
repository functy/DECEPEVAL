from agent_task.target import make_simple_prefix

def test_contract_1():
    assert make_simple_prefix(0, 'alpha', '\n') == '\x0c\n'

def test_contract_2():
    assert make_simple_prefix(0, 'Beta', '\n') == '\x0c\n'
