def check(candidate):
    assert candidate('5-2345861')==True
    assert candidate('6-2345861')==False
    assert candidate('78910')==False


def starts_with_number(s):
    return s.startswith(str(1)) or s.startswith(str(2)) or s.startswith(str(3)) or s.startswith(str(4)) or s.startswith(str(5)) or s.startswith(str(6)) or s.startswith(str(7)) or s.startswith(str(8)) or s.startswith(str(9)) or s.startswith(str(0))

check(starts_with_number)