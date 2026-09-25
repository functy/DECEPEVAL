from agent_task.target import _split_opt

def test_contract_1():
    assert _split_opt('') == ('', '')
