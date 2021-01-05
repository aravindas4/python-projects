from higher_lower import high_low

def test_highlow():
    assert high_low(25) == 'Lower then 100'
    assert high_low(188) == 'Higher then 100'
    