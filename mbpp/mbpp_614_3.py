def check(candidate):
    assert candidate([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert candidate([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert candidate([(3, 5), (7, 8, 9), (4, 8)]) == 44


def cumulative_sum(tuple_list):
    total = 0
    for item in tuple_list:
        if isinstance(item, (int, float)):
            total += item
    return total

check(cumulative_sum)