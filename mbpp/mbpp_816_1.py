def check(candidate):
    assert candidate((1, 5, 3, 6, 8)) == ()
    assert candidate((2, 1, 4 ,5 ,6)) == ()
    assert candidate((3, 2, 5, 6, 8)) == ()


def clear_tuple_values(t):
    return ()

check(clear_tuple_values)