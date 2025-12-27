def check(candidate):
    assert candidate([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
    assert candidate([[0,1,1],[1,1,2],[3,2,1]]) == 6
    assert candidate([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19


def max_sum_of_lists(list_of_lists):
    if not list_of_lists:
        return 0
    max_sum = -float('inf')
    for sublist in list_of_lists:
        if not sublist:
            continue
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

check(max_sum_of_lists)