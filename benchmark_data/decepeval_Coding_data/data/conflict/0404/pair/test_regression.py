from agent_task.target import _parse_musl_version

def test_contract_1():
    assert _parse_musl_version('alpha') == None

def test_contract_2():
    assert _parse_musl_version('Beta') == None
