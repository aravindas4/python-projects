from num_calculation import calculator

def test_calculator():
    assert calculator("+",89,71,True) == 160
    assert calculator("+",10,28,False) == 38
    assert calculator("sub",13,53,True) == 40
    assert calculator("-",29,22,False) == 7
    assert calculator("mul",26,40,False) != 1400
    assert calculator("*",34,3,True) == 102
    assert calculator("/",6,48,True) == 8
    assert calculator("div",88,4,False) == 22
    