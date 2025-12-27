def check(candidate):
    assert candidate([1,2,4,5],6)==4
    assert candidate([1,2,4,5],3)==2
    assert candidate([1,2,4,5],7)==4


def find_left_insertion_point(sorted_list, value):
    left = 0
    right = len(sorted_list)
    
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

check(find_left_insertion_point)