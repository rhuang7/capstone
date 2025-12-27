def check(candidate):
    assert candidate([-4,-3,-2,-1]) == True
    assert candidate([1,2,3]) == True
    assert candidate([3,2,1]) == False


def is_decreasing_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            return False
    return True

check(is_decreasing_sequence)