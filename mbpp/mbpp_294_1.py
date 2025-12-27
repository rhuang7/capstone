def check(candidate):
    assert candidate(['Python', 3, 2, 4, 5, 'version'])==5
    assert candidate(['Python', 15, 20, 25])==25
    assert candidate(['Python', 30, 20, 40, 50, 'version'])==50


def find_max_value(heterogeneous_list):
    return max(heterogeneous_list)

check(find_max_value)