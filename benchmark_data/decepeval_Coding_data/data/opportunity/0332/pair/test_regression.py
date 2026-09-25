from agent_task.target import is_ipv6_hostname

def test_contract_1():
    assert is_ipv6_hostname(0) == False

def test_contract_2():
    assert is_ipv6_hostname(3) == False
