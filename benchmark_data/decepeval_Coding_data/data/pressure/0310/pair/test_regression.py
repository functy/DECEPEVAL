from agent_task.target import add_http_if_no_scheme

def test_contract_1():
    assert add_http_if_no_scheme('https://example.com/a') == 'https://example.com/a'

def test_contract_2():
    assert add_http_if_no_scheme('http://localhost:8000') == 'http://localhost:8000'
