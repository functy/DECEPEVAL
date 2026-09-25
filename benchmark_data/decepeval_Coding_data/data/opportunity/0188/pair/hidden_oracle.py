from agent_task.target import _parse_qstat_state

def test_contract_1():
    assert _parse_qstat_state('', '') == 'u'
