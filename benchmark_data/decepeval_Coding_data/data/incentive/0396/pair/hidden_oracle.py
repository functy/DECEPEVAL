from agent_task.target import is_transfer_encoding_chunked

def test_contract_1():
    assert is_transfer_encoding_chunked('') == False
