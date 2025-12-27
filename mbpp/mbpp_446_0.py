def check(candidate):
    assert candidate(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert candidate((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert candidate((1,2,3,4,5,6),[1,2]) == 2


def count_elements_in_tuple(lst, tup):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in tup:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

check(count_elements_in_tuple)