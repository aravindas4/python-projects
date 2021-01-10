from convert_input import car_info

def test_defs():
    assert car_info(2018,'Purple','Nano','XMA') == '2018 Purple Nano XMA.'
    