def check(candidate):
    assert candidate([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
    assert candidate([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(1,[1])
    assert candidate([[3,4,5],[6,7,8,9],[10,11,12],[1,2]])==(2,[1,2])


def find_min_length_list(lists):
    return min(lists, key=lambda x: len(x))

check(find_min_length_list)