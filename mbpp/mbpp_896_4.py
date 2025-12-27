def check(candidate):
    assert candidate([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])==[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
    assert candidate([(9,8), (4, 7), (3,5), (7,9), (1,2)])==[(1,2), (3,5), (4,7), (9,8), (7,9)] 
    assert candidate([(20,50), (10,20), (40,40)])==[(10,20),(40,40),(20,50)] 


def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

check(sort_by_last_element)