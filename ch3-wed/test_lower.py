from higher_lower import lower

def test_low():
    assert lower(19,28) == 'lower'
    assert lower(98,12) == 'lower'
    