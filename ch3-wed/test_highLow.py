from higher_lower import *

def test_highlow():
    assert high_low(25) == 'Lower then 100'
    assert high_low(188) == 'Higher then 100'
    
def test_low():
    assert lower(19,28) == 'lower'
    assert lower(98,12) == 'lower'