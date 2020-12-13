from area_cal import add

def test_area():
    a = 254.44
    b = 13.66
    area = a * b
    assert add(a,b) == area

