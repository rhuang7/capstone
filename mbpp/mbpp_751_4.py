def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6], 0) == True
    assert candidate([2, 3, 4, 5, 10, 15], 0) == True
    assert candidate([2, 10, 4, 5, 3, 15], 0) == False


def is_min_heap(arr):
    def is_min_heap_util(index):
        # Check if the current node is smaller than its children
        left = 2 * index + 1
        right = 2 * index + 2

        # If left child is out of bounds, no need to check
        if left >= len(arr):
            return True

        # If right child is out of bounds, check only left
        if right >= len(arr):
            return arr[index] <= arr[left]

        # Check both children
        return arr[index] <= arr[left] and arr[index] <= arr[right]

    # Start checking from the root (index 0)
    for i in range(len(arr)):
        if not is_min_heap_util(i):
            return False
    return True

check(is_min_heap)