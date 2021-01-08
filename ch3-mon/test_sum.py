from convert_input import sum

def test_add():
    assert sum(87,38) == 125
    assert sum(56,98) != 144
    