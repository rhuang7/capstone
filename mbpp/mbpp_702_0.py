def check(candidate):
    assert candidate([1, 3, 4, 9, 10,11, 12, 17, 20], 9, 4) == 5
    assert candidate([1, 5, 6, 2, 8], 5, 2) == 3
    assert candidate([1, 2, 3 ,4, 5, 6], 6, 3) == 2


def min_removals_to_satisfy_range(arr, k):
    from collections import deque
    import heapq

    if not arr:
        return 0

    # Sort the array to easily find amin and amax
    arr.sort()
    n = len(arr)

    # Use a sliding window to find the longest subarray where amax - amin <= k
    left = 0
    max_len = 0

    for right in range(n):
        # Maintain a window where the difference between max and min is <= k
        # Use a deque to track the max and min in the window
        while arr[right] - arr[left] > k:
            left += 1

        # Update the maximum window size
        max_len = max(max_len, right - left + 1)

    # The minimum number of elements to remove is total elements - max window size
    return n - max_len

check(min_removals_to_satisfy_range)