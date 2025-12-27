def check(candidate):
    assert candidate([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert candidate([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert candidate([0,1,0,1,1]) == [1,1,1,0,0]


def move_zeroes(lst):
    # Initialize two pointers
    left = 0
    right = 0
    
    # Iterate through the list
    while right < len(lst):
        # If the element at right is not zero, swap it with the element at left
        if lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        right += 1
    
    return lst

check(move_zeroes)