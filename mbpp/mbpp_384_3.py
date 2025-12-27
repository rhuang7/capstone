def check(candidate):
    assert candidate(5,[1,2,3,4,3]) == 1
    assert candidate(7,[3,1,2,5,6,2,3]) == 1
    assert candidate(7,[3,3,6,3,7,4,9]) == 3


def frequency_of_smallest(arr):
    if not arr:
        return 0
    smallest = min(arr)
    return arr.count(smallest)

check(frequency_of_smallest)