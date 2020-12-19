from ch2-wed2 import format_ch2

def test_format():
    assert "{}'s favorite sports is {}".format(name,sport) == "Anand's favorite sports is Cricket"
    assert "{} is working on {} programming".format(name,program) == "Anand is working on python programming"
