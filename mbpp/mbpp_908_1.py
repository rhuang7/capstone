def check(candidate):
    assert candidate([-10, -1, 0, 3, 10, 11, 30, 50, 100],9) == 3
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8],8) == -1
    assert candidate([0, 2, 5, 8, 17],5) == 0


def find_fixed_point(arr):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1

check(find_fixed_point)