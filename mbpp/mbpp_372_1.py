def check(candidate):
    assert candidate([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==[1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 18]
    assert candidate([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert candidate([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

check(heap_sort)