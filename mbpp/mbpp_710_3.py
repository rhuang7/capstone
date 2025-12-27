def check(candidate):
    assert candidate((10, 4, 5, 6, 7)) == (10, 7)
    assert candidate((1, 2, 3, 4, 5)) == (1, 5)
    assert candidate((6, 7, 8, 9, 10)) == (6, 10)


def get_initial_and_last(data):
    if not data:
        return None, None
    return data[0], data[-1]

check(get_initial_and_last)