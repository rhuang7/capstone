def check(candidate):
    assert candidate(9) == 49
    assert candidate(10) == 66
    assert candidate(11) == 88


def sum_perrin_numbers(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    if n == 2:
        return 0
    perrin = [3, 0, 2]
    for i in range(3, n + 1):
        perrin.append(perrin[i-2] + perrin[i-3])
    return sum(perrin)

check(sum_perrin_numbers)