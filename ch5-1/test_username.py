from user_name import *

def test_check_uppercase():
    assert uppercase("Hello") == True
    assert uppercase("django") == False

def test_no_name():
    assert name("Anand","S") == "Anand S"
    assert name() == "No name passed in"