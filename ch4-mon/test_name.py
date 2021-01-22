from issue_names import *

def test_sport():
    assert string(["Chess","Carrom","Ludo"]) == "I like to play Chess, I like to play Carrom, I like to play Ludo"

def test_letter():
    assert group(["Raj","Ajey", "Madhu", "Ananth"]) == "R,A,M,A"