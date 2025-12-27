def check(candidate):
    assert candidate((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert candidate((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert candidate((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}


def tuple_to_dict(t):
    if len(t) % 2 != 0:
        raise ValueError("Tuple length must be even")
    return {t[i]: t[i+1] for i in range(0, len(t), 2)}

check(tuple_to_dict)