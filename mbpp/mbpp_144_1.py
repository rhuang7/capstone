def check(candidate):
    assert candidate([1,8,9,15,16],5) == 74
    assert candidate([1,2,3,4],4) == 10
    assert candidate([1,2,3,4,5,7,9,11,14],9) == 188


def sum_of_absolute_differences(arr):
    arr.sort()
    total = 0
    for i in range(len(arr)):
        total += arr[i] * i - sum(arr[:i])
    return total

check(sum_of_absolute_differences)