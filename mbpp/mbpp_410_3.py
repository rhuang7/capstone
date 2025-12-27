def check(candidate):
    assert candidate(['Python', 3, 2, 4, 5, 'version'])==2
    assert candidate(['Python', 15, 20, 25])==15
    assert candidate(['Python', 30, 20, 40, 50, 'version'])==20


def find_min_value(heterogeneous_list):
    return min(heterogeneous_list)

check(find_min_value)