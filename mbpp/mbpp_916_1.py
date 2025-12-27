def check(candidate):
    assert candidate([1, 4, 45, 6, 10, 8], 6, 22) == (4, 10, 8)
    assert candidate([12, 3, 5, 2, 6, 9], 6, 24) == (12, 3, 9)
    assert candidate([1, 2, 3, 4, 5], 5, 9) == (1, 3, 5)


def has_triplet_sum(arr, target):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return False

check(has_triplet_sum)