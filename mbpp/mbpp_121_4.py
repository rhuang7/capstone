def check(candidate):
    assert candidate([2, 7, 4, 0, 9, 5, 1, 3], 8, 6, 0) == True
    assert candidate([1, 4, 5, 6, 7, 8, 5, 9], 8, 6, 0) == False
    assert candidate([10, 4, 2, 3, 5], 5, 15, 0) == True


def find_triplet_with_sum(arr, target_sum):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return (arr[i], arr[left], arr[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return None

check(find_triplet_with_sum)