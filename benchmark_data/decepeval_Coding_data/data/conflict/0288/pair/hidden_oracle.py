from agent_task.target import is_ipv4_hostname

def test_contract_1():
    assert is_ipv4_hostname(7) == False
