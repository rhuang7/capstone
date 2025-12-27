def check(candidate):
    assert candidate((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    assert candidate((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
    assert candidate((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)


def divide_tuples(tuples):
    result = []
    for a, b in tuples:
        if b == 0:
            result.append("Error: division by zero")
        else:
            result.append(a / b)
    return result

check(divide_tuples)