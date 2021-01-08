from issue_check import check_es

def test_es():
    assert check_es('Includes') != False
    assert check_es('Assess') == True
    assert check_es('excersise') == False