def check(candidate):
    assert candidate(([1, 2, [3,4],[5,6]]))==21
    assert candidate(([7, 10, [15,14],[19,41]]))==106
    assert candidate(([10, 20, [30,40],[50,60]]))==210


def recursive_list_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_list_sum(lst[1:])

check(recursive_list_sum)