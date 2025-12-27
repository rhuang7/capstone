def check(candidate):
    assert candidate({10})==False
    assert candidate({11})==False
    assert candidate({})==True


def is_dict_empty(d):
    return len(d) == 0

check(is_dict_empty)