def check(candidate):
    assert candidate([(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )], 4) == True
    assert candidate([(7, 7, 7), (7, 7)], 7) == True
    assert candidate([(9, 9), (9, 9, 9, 9)], 7) == False


def has_all_k_elements(tuples_list, k):
    elements = set()
    for t in tuples_list:
        elements.update(t)
    return len(elements) == k

check(has_all_k_elements)