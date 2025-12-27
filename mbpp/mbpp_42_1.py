def check(candidate):
    assert candidate([1,2,3,1,1,4,5,6],8) == 3
    assert candidate([1,2,3,1,1],5) == 3
    assert candidate([1,1,2],3) == 2


def sum_of_repeated_elements(arr):
    from collections import Counter
    count = Counter(arr)
    return sum(value * key for key, value in count.items() if value > 1)

check(sum_of_repeated_elements)