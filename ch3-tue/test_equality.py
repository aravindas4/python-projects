from issue_check import equality

def test_equa():
    assert equality('Code','coDE') == 'Both words are same'
    assert equality('pYtHoN','PyThOn') != 'Both are different words'
    