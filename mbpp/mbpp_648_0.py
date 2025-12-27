def check(candidate):
    assert candidate([0,1,2,3,4,5])==[1, 0, 3, 2, 5, 4] 
    assert candidate([5,6,7,8,9,10])==[6,5,8,7,10,9] 
    assert candidate([25,35,45,55,75,95])==[35,25,55,45,95,75] 


def swap_adjacent_pairs(lst):
    # Convert the list to a mutable sequence (list)
    lst = list(lst)
    # Iterate through the list in steps of 2
    for i in range(0, len(lst) - 1, 2):
        # Swap the current element with the next one
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

check(swap_adjacent_pairs)