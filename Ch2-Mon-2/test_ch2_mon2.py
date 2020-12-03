from type_check import ch_one

def test_ch_one():
    assert ch_one(2) == int
    assert ch_one(4+5.9) == float
    assert ch_one(5.0) == float
    assert ch_one(True and False) == bool
    first_name = 'Anand'
    last_name = 'S'
    assert ch_one(f'{first_name} {last_name}') == str
