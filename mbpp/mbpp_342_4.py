def check(candidate):
    assert candidate([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]) == (4, 6)
    assert candidate([[ 2, 3, 4, 8, 10, 15 ], [1, 5, 12], [7, 8, 15, 16], [3, 6]]) == (4, 7)
    assert candidate([[4, 7, 9, 11, 16], [2, 6, 13], [5, 9, 16, 17], [3, 7]]) == (5, 7)


def smallest_range(arrays):
    import heapq
    from itertools import product

    # Create a list of tuples (value, array_index, element_index)
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    current_max = max(arr[0] for arr in arrays if arr)

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        if val > current_max:
            current_max = val
        if len(result) == 0 or current_max - val < result[1] - result[0]:
            result = [val, current_max]

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
        else:
            break

    return result if result else []

check(smallest_range)