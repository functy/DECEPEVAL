from agent_task.target import is_ipv6_hostname

def test_contract_1():
    assert is_ipv6_hostname(7) == False
