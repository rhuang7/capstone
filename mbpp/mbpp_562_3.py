def check(candidate):
    assert candidate([[1],[1,4],[5,6,7,8]]) == 4
    assert candidate([[0,1],[2,2,],[3,2,1]]) == 3
    assert candidate([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5


def max_sublist_length(lists):
    if not lists:
        return 0
    max_len = 0
    for sublist in lists:
        if len(sublist) > max_len:
            max_len = len(sublist)
    return max_len

check(max_sublist_length)