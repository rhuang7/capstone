def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
    assert candidate([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert candidate([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]


def reverse_array_up_to_position(arr, position):
    # Check if position is valid
    if position < 0 or position >= len(arr):
        return arr  # Return original array if position is out of bounds
    
    # Reverse the array up to the given position
    arr[:position+1] = arr[:position+1][::-1]
    return arr

check(reverse_array_up_to_position)