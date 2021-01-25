from div3_vowel import *

def test_division():
    assert division(100) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

def test_vowels():
    assert select("Visual STUDIO code") == "iuauiooe"
    assert select("Animation") == "aiaio"
