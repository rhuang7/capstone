def check(candidate):
    assert candidate([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]
    assert candidate([32, 14, 5, 6, 7, 19]) == [5, 6, 7, 14, 19, 32]
    assert candidate([21, 15, 29, 78, 65]) == [15, 21, 29, 65, 78]


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

check(heap_sort)