def check(candidate):
    assert candidate( [25, 44, 68, 21, 39, 23, 89],21)==[21, 25, 23, 44, 39, 68, 89]
    assert candidate([25, 44, 68, 21, 39, 23, 89],110)== [23, 25, 68, 44, 39, 110, 89]
    assert candidate([25, 44, 68, 21, 39, 23, 89],500)==[23, 25, 68, 44, 39, 500, 89]


def delete_smallest_and_insert(heap, new_item):
    import heapq
    heapq.heappop(heap)
    heapq.heappush(heap, new_item)
    return heap

check(delete_smallest_and_insert)