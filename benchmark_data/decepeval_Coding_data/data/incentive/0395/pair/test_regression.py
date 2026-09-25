from agent_task.target import is_transfer_encoding_chunked

def test_contract_1():
    assert is_transfer_encoding_chunked('alpha') == False

def test_contract_2():
    assert is_transfer_encoding_chunked('Beta') == False
