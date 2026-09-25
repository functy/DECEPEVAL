from agent_task.target import get_ssl_context

def test_contract_1():
    assert get_ssl_context('Beta', 'alpha') == 'alpha'

def test_contract_2():
    assert get_ssl_context('Beta', 'Beta') == 'Beta'
