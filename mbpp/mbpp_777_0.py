def check(candidate):
    assert candidate([1,2,3,1,1,4,5,6],8) == 21
    assert candidate([1,10,9,4,2,10,10,45,4],9) == 71
    assert candidate([12,10,9,45,2,10,10,45,10],9) == 78


def sum_of_non_repeated_elements(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] += 1
    total = 0
    for num in arr:
        if frequency[num] == 1:
            total += num
    return total

check(sum_of_non_repeated_elements)