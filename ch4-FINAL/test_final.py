import final_issue

def test_name():
    assert final_issue.extract(['John', ' ', 'Amanda', 5]) == ['John', 'Amanda']
    assert final_issue.extract(['A',2,'B','4']) == ["A","B"]

def test_fahrenheit():
    assert final_issue.temperature([32, 12, 44, 29]) == [89.6, 53.6, 111.2, 84.2]
    assert final_issue.temperature([19, 86, 72, 35]) == [66.2, 186.8, 161.6, 95.0]
    