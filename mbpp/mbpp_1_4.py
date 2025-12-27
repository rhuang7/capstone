def check(candidate):
    assert candidate([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2) == 8
    assert candidate([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2) == 12
    assert candidate([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2) == 16


def min_cost_path(cost, m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0 and n == 0:
        return cost[0][0]
    return cost[m][n] + min(
        min_cost_path(cost, m - 1, n),
        min_cost_path(cost, m, n - 1)
    )

check(min_cost_path)