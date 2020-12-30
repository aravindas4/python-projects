from convert_input import *

def test_defs():
    assert con_bool("Hello") == bool
    assert con_bool('') == bool
    assert con_bool(8) == bool
    assert sum(23,45) == 68
    assert car_info(2018,'Purple','Nano','XMA') == '2018 Purple Nano XMA.'
    