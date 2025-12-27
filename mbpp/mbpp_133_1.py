def check(candidate):
    assert candidate([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
    assert candidate([10,15,-14,13,-18,12,-20])==-52
    assert candidate([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894


def sum_of_negatives(numbers):
    return sum(map(lambda x: x if x < 0 else 0, numbers))

check(sum_of_negatives)