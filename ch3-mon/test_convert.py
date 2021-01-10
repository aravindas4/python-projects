from convert_input import con_bool

def test_bool():
    assert con_bool('Python') == bool
    assert con_bool('') == bool
    assert con_bool(88) == bool
    