def check(candidate):
    assert candidate([3,2,1]) == False
    assert candidate([1,2,3]) == False
    assert candidate([2,1,4]) == True


def has_even_numbers_at_even_indices(lst):
    for i in range(0, len(lst), 2):
        if i >= len(lst):
            break
        if lst[i] % 2 != 0:
            return False
    return True

check(has_even_numbers_at_even_indices)