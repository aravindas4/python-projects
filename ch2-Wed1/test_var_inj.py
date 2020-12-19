from variable_injctn  import injection

def test_inject():
    assert injection(1, 2, 3) == "1 2 3"
    assert injection(1, 2, 3) != "1, 2, 3"
    assert injection('A', 8888, 'Hi there', True) == "A 8888 Hi there True"
    assert injection(True, False) == 'True False'