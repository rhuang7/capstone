def check(candidate):
    assert candidate([1,1,2,2,3],5) == 3
    assert candidate([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    assert candidate([1,2,2,3,3,4,4],7) == 1


def find_single_element(sorted_array):
    left = 0
    right = len(sorted_array) - 1

    while left < right:
        mid = (left + right) // 2

        # If the middle element is the same as the next, the single element is after
        if sorted_array[mid] == sorted_array[mid + 1]:
            left = mid + 2
        # If the middle element is the same as the previous, the single element is before
        elif sorted_array[mid] == sorted_array[mid - 1]:
            right = mid - 1
        # Otherwise, the single element is at mid
        else:
            return sorted_array[mid]

    return sorted_array[left]

check(find_single_element)