from agent_task.target import unquote_unreserved

def test_contract_1():
    assert unquote_unreserved('http://localhost:8000') == 'http://localhost:8000'
