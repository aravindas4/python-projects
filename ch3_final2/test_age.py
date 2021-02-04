from issue_age import group

def test_age():
    assert group(12) == "Kid"
    assert group(19) == "Teenager"
    assert group(28) == "Young Adult"
    assert group(64) == "Adult"
    assert group(65) == "Senior"
