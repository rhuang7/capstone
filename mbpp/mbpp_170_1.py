def check(candidate):
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38


def sum_between_indices(lst, start, end):
    return sum(lst[start:end])

check(sum_between_indices)