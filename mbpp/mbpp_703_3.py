def check(candidate):
    assert candidate({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)==True
    assert candidate({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},6)==True
    assert candidate({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)==False


def is_key_present(d, key):
    return key in d

check(is_key_present)