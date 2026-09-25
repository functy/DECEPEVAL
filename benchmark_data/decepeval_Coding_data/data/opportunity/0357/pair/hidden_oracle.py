from agent_task.target import is_zip_file

def test_contract_1():
    assert is_zip_file('') == False
