def check(candidate):
    assert candidate(["red", "black", "white", "green", "orange"])==['red', 'white', 'orange']
    assert candidate([2, 0, 3, 4, 0, 2, 8, 3, 4, 2])==[2, 3, 0, 8, 4]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]


def alternate_elements(input_list):
    result = []
    for i in range(0, len(input_list), 2):
        result.append(input_list[i])
    return result

check(alternate_elements)