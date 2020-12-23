from variable_injctn  import variable

def test_inject():
    assert variable(28,20.8,True,'A') == "28 20.8 True A"
    assert variable(19,False,True,91.0) != "91 True False 19.0"
    assert variable('Any',True,8) == "Any True 8"
    assert variable('A', 8888, 'Hi there', True) == "A 8888 Hi there True"
    assert variable(True, False,80.0) != 'True False 80'