def check(candidate):
    assert candidate([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
    assert candidate([[1], [5, 7], [10, 12, 14,15]])==(1, [1])
    assert candidate([[5], [15,20,25]])==(1, [5])


def find_min_length_lists(lists):
    if not lists:
        return []
    
    min_length = min(len(lst) for lst in lists)
    return [lst for lst in lists if len(lst) == min_length]

check(find_min_length_lists)