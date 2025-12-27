def check(candidate):
    assert candidate([1,2,3,4]) == True
    assert candidate([4,3,2,1]) == False
    assert candidate([0,1,4,9]) == True


def is_increasing(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            return False
    return True

check(is_increasing)