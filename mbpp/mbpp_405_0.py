def check(candidate):
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True


def element_in_tuple(element, tup):
    return element in tup

check(element_in_tuple)