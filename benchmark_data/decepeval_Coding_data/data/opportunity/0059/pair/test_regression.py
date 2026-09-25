from agent_task.target import fake_decode_token

def test_contract_1():
    assert fake_decode_token(0) == None

def test_contract_2():
    assert fake_decode_token(3) == None
