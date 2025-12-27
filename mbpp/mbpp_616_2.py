def check(candidate):
    assert candidate((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert candidate((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert candidate((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)


def modulo_tuples(tuple1, tuple2):
    result = []
    for a, b in zip(tuple1, tuple2):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result.append(a % b)
    return tuple(result)

check(modulo_tuples)