from higher_lower import *

def test_highlow():
    assert high_low(25) == 'Lower than 100'
    assert high_low(188) == 'Higher than 100'
    
def test_low():
    assert lower(19,28) == 'lower'
    assert lower(78,34) != 'lower'