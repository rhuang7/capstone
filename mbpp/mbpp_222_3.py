def check(candidate):
    assert candidate((5, 6, 7, 3, 5, 6) ) == True
    assert candidate((1, 2, "4") ) == False
    assert candidate((3, 2, 1, 4, 5) ) == True


def all_same_data_type(t):
    if not t:
        return True  # Empty tuple is considered to have all elements of the same type
    first_type = type(t[0])
    for element in t:
        if type(element) != first_type:
            return False
    return True

check(all_same_data_type)