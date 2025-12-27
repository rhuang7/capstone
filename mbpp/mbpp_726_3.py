def check(candidate):
    assert candidate((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert candidate((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert candidate((12, 13, 14, 9, 15)) == (156, 182, 126, 135)


def multiply_adjacent_elements(t):
    result = 1
    for i in range(len(t) - 1):
        result *= t[i] * t[i + 1]
    return result

check(multiply_adjacent_elements)