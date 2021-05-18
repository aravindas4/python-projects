from user_dict import create_dict

def test_dict():
    assert create_dict("Jay",27) == {"Name":"Jay", "Age":27}