from uppercase_strip import strip_symbols

def test_strip():
      assert strip_symbols("&good morning&") == "good morning"
      assert strip_symbols('^Hell0^') != 'Hello'
      assert strip_symbols('................Dots.............') == 'Dots'
      