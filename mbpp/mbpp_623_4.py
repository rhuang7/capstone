def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate([10,20,30],3)==([1000, 8000, 27000])
    assert candidate([12,15],5)==([248832, 759375])


def nth_power_of_list_elements(lst, n):
    return list(map(lambda x: x ** n, lst))

check(nth_power_of_list_elements)