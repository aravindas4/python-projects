from uppercase_strip import uppercase

def test_function():
    assert uppercase("LowerCase") == "LOWERCASE"
    assert uppercase('UPPERCA5E') != 'UPPERCASE'
    assert uppercase('make it uppercase') == 'MAKE IT UPPERCASE'
    