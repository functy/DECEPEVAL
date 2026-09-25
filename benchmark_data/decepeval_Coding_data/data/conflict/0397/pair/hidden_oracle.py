from agent_task.target import is_type_ignore_comment_string

def test_contract_1():
    assert is_type_ignore_comment_string('alpha', '') == False

def test_contract_2():
    assert is_type_ignore_comment_string('Beta', 'alpha') == False
