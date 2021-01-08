from issue_check import exponent

def test_exponent():
    assert exponent(8) == 64
    assert exponent(10) != 100
    assert exponent(13) == 13