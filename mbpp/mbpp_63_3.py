def check(candidate):
    assert candidate([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert candidate([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert candidate([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23


def max_difference_in_pairs(tup_list):
    if not tup_list or len(tup_list) < 2:
        return 0
    
    max_diff = 0
    for i in range(len(tup_list)):
        for j in range(i + 1, len(tup_list)):
            diff = abs(tup_list[i] - tup_list[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

check(max_difference_in_pairs)