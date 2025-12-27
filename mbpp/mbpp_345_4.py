def check(candidate):
    assert candidate([1, 1, 3, 4, 4, 5, 6, 7])==[0, 2, 1, 0, 1, 1, 1]
    assert candidate([4, 5, 8, 9, 6, 10])==[1, 3, 1, -3, 4]
    assert candidate([0, 1, 2, 3, 4, 4, 4, 4, 5, 7])==[1, 1, 1, 1, 0, 0, 0, 1, 2]


def find_number_differences(numbers):
    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i-1])
    return differences

check(find_number_differences)