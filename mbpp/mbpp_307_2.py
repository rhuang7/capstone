def check(candidate):
    assert candidate(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
    assert candidate(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert candidate(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)


def get_colon_of_tuple(t):
    if not isinstance(t, tuple):
        raise ValueError("Input must be a tuple")
    if len(t) < 2:
        raise ValueError("Tuple must have at least two elements")
    return t[0] + ":" + t[1]

check(get_colon_of_tuple)