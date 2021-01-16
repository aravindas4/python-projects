from error_time import *

def test_fix():
    assert fix("John") == "Hello John"
    assert fix("Ajay") == None

def test_military():
    assert military_time(1800) == "Good Evening"
    assert military_time(1428) == "Good Afternoon"
    assert military_time(848) == "Good Morning"
    