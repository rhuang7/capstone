def check(candidate):
    assert candidate([1,2,0,1,0,1,2,1,1], 9) == [0, 0, 1, 1, 1, 1, 1, 2, 2]
    assert candidate([1,0,0,1,2,1,2,2,1,0], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
    assert candidate([2,2,1,0,0,0,1,1,2,1], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]


def sort_array(arr):
    # Count occurrences of 0, 1, and 2
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    # Create a new list with the sorted order
    sorted_arr = [0] * count_0 + [1] * count_1 + [2] * count_2
    
    return sorted_arr

check(sort_array)