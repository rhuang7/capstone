def check(candidate):
    assert candidate([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert candidate([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert candidate([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]


def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        # Find the index of the maximum element in arr[0..size-1]
        max_idx = 0
        for i in range(1, size):
            if arr[i] > arr[max_idx]:
                max_idx = i
        # Put the maximum element at the end
        if max_idx != size - 1:
            # Flip the array from 0 to max_idx
            arr[:max_idx+1] = reversed(arr[:max_idx+1])
            # Flip the array from 0 to size-1
            arr[:size] = reversed(arr[:size])
    return arr

check(pancake_sort)