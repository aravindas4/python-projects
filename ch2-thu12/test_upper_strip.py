from uppercase_strip import uppercase,strip_symbols

def test_function():
    assert uppercase("LowerCase") == "LOWERCASE"
    assert strip_symbols("&good morning&") == "good morning"
    