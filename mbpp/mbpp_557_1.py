def check(candidate):
    assert candidate("Python")==("pYTHON")
    assert candidate("Pangram")==("pANGRAM")
    assert candidate("LIttLE")==("liTTle")


def toggle_case(s):
    return s.swapcase()

check(toggle_case)