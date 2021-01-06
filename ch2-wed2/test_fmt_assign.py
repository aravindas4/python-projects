from format_assign import format

def test_assign():
    a = "Dhanush's favorite sports is hockey."
    b = "Dhanush is working on java programming!"
    c = a+"\n"+b
    assert format("Dhanush","hockey","java") == c
