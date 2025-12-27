def check(candidate):
    assert candidate(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert candidate(([1, 2], [3, 4], [5, 6]))  == 3
    assert candidate(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1


def count_lists_in_tuple(input_tuple):
    count = 0
    for item in input_tuple:
        if isinstance(item, list):
            count += 1
    return count

check(count_lists_in_tuple)