def check(candidate):
    assert candidate([12,3,5,7,19], 5, 2) == 3
    assert candidate([17,24,8,23], 4, 3) == 8
    assert candidate([16,21,25,36,4], 5, 4) == 36


def find_kth_element(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    return arr[k - 1]

check(find_kth_element)