from issue_check import check_ing

def test_ing():
    assert check_ing('Coding') == True
    assert check_ing('English') == False
    assert check_ing('kings') != True