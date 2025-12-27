def check(candidate):
    assert candidate([1, 2, 3, 4, 1, 2, 3]) == 3
    assert candidate([-7, 1, 5, 2, -4, 3, 0]) == 3
    assert candidate([1, 2, 3]) == -1


def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1

check(find_equilibrium_index)