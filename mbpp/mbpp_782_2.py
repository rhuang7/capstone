def check(candidate):
    assert candidate([1,2,4]) == 14
    assert candidate([1,2,1,2]) == 15
    assert candidate([1,7]) == 8


def sum_of_odd_length_subarrays(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if (j - i) % 2 == 1:
                subarray = arr[i:j]
                total += sum(subarray)
    return total

check(sum_of_odd_length_subarrays)