def check(candidate):
    assert candidate([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert candidate([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert candidate([[5], [15,20,25]])==(3, [15,20,25])


def find_max_length_lists(lists):
    if not lists:
        return []
    max_len = max(len(lst) for lst in lists)
    return [lst for lst in lists if len(lst) == max_len]

check(find_max_length_lists)