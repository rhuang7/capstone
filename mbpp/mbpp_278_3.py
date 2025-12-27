def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10) ) == 3
    assert candidate((2, 9, (5, 7), 11) ) == 2
    assert candidate((11, 15, 5, 8, (2, 3), 8) ) == 4


def count_before_record(tup):
    if not tup:
        return 0
    count = 0
    for i in range(len(tup)):
        if i > 0 and tup[i] == tup[i-1]:
            count += 1
    return count

check(count_before_record)