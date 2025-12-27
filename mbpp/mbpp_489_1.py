def check(candidate):
    assert candidate(5,[1,2,3,4,4]) == 2
    assert candidate(3,[5,6,5]) == 1
    assert candidate(4,[2,7,7,7]) == 3


def frequency_of_largest_value(arr):
    if not arr:
        return 0
    max_value = max(arr)
    return arr.count(max_value)

check(frequency_of_largest_value)