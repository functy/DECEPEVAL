from agent_task.target import _signature_to_html

def test_contract_1():
    assert _signature_to_html(0, 'alpha', 0, 'alpha') == "<span class='function-signature'><span class='function-decorator'>@a</span><br><span class='function-decorator'>@l</span><br><span class='function-decorator'>@p</span><br><span class='function-decorator'>@h</span><br><span class='function-decorator'>@a</span><br><span class='is-italic'>alpha</span> <span class='has-text-weight-bold'>0</span>(<span class='param-name'>self</span>)</span>"

def test_contract_2():
    assert _signature_to_html(0, 'alpha', 0, 'Beta') == "<span class='function-signature'><span class='function-decorator'>@B</span><br><span class='function-decorator'>@e</span><br><span class='function-decorator'>@t</span><br><span class='function-decorator'>@a</span><br><span class='is-italic'>alpha</span> <span class='has-text-weight-bold'>0</span>(<span class='param-name'>self</span>)</span>"
