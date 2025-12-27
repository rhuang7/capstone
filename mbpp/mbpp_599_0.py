def check(candidate):
    assert candidate(10)==(55, 5.5)
    assert candidate(15)==(120, 8.0)
    assert candidate(20)==(210, 10.5)


def calculate_sum_and_average(n):
    if n < 1:
        return (0, 0.0)
    total = n * (n + 1) // 2
    average = total / n
    return (total, average)

check(calculate_sum_and_average)