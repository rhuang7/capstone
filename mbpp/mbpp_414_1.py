def check(candidate):
    assert candidate([1,2,3,4,5],[6,7,8,9]) == False
    assert candidate([1,2,3],[4,5,6]) == False
    assert candidate([1,4,5],[1,4,5]) == True


def value_in_sequence(value, sequence):
    return value in sequence

check(value_in_sequence)