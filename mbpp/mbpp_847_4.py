def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]
    assert candidate([4, 8, 2, 10, 15, 18]) == [4, 8, 2, 10, 15, 18]
    assert candidate([4, 5, 6]) == [4, 5, 6]



def copy_from_singleton_tuple(t):
    if len(t) != 1:
        raise ValueError("Input must be a singleton tuple")
    return [t[0]]

check(copy_from_singleton_tuple)