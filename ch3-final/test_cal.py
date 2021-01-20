from num_calculation import calculator

def test_calculator():
    assert calculator("+",89,71,"r") == 160
    assert calculator("+",10,28,None) == 38
    assert calculator("sub",13,53,'r') == 40
    assert calculator("-",29,22,None) == 7
    assert calculator("mul",26,40,None) != 1400
    assert calculator("*",34,3,"r") == 102
    assert calculator("/",6,48,"r") == 8
    assert calculator("div",88,4,None) == 22