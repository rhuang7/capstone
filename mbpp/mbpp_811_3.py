def check(candidate):
    assert candidate([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True
    assert candidate([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False
    assert candidate([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True


def are_lists_of_tuples_identical(list1, list2):
    return list1 == list2

check(are_lists_of_tuples_identical)