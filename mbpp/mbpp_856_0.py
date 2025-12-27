def check(candidate):
    assert candidate([1,0,1,0],4) == 3
    assert candidate([0,1,0],3) == 1
    assert candidate([0,0,1,1,0],5) == 2


def min_adjacent_swaps_to_sort_binary(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        if arr[i] == 0:
            continue
        for j in range(i + 1, n):
            if arr[j] == 0:
                swaps += 1
                arr[i], arr[j] = arr[j], arr[i]
                break
    return swaps

check(min_adjacent_swaps_to_sort_binary)