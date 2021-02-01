from rem_dupl import *

def test_duplicate():
    assert duplicate(['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']) == ["Bob","Kenny","Amanda"]
    assert duplicate(["Mon", "tue", "thu", "wed","Mon", "thu"]) == ["Mon","tue","thu","wed"]
