def check(candidate):
    assert candidate([1,2,3],4) == 0
    assert candidate([1,2,2,3,3,3,4],3) == 3
    assert candidate([0,1,2,3,1,2],1) == 2


def number_frequency(arr, num):
    return arr.count(num)

check(number_frequency)