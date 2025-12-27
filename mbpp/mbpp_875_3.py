def check(candidate):
    assert candidate([(3, 5), (1, 7), (10, 3), (1, 2)]) == 1
    assert candidate([(4, 6), (12, 8), (11, 4), (2, 13)]) == 2
    assert candidate([(5, 17), (3, 9), (12, 5), (3, 24)]) == 6


def min_difference_in_tuple_pairs(tuples):
    if not tuples or len(tuples) < 2:
        return 0  # or raise an error if empty input is not allowed
    
    min_diff = float('inf')
    
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            diff = abs(tuples[i][0] - tuples[j][0]) + abs(tuples[i][1] - tuples[j][1])
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

check(min_difference_in_tuple_pairs)