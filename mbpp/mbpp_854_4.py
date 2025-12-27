def check(candidate):
    assert candidate([25, 44, 68, 21, 39, 23, 89])==[21, 25, 23, 44, 39, 68, 89]
    assert candidate([25, 35, 22, 85, 14, 65, 75, 25, 58])== [14, 25, 22, 25, 35, 65, 75, 85, 58]
    assert candidate([4, 5, 6, 2])==[2, 4, 6, 5]


def heapify(lst):
    import heapq
    heapq.heapify(lst)

check(heapify)