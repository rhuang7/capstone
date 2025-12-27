def check(candidate):
    assert candidate((1,5,3,19,18,25),6) == 1
    assert candidate((4,3,2,6),4) == 1
    assert candidate((30,5,20,9),4) == 4


def min_difference(arr):
    if len(arr) < 2:
        return 0  # or raise an error, but per task, return 0 for less than 2 elements
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

check(min_difference)