def check(candidate):
    assert candidate([1,2,'abc',1.2]) == 2
    assert candidate([1,2,3]) == 3
    assert candidate([1,1.2,4,5.1]) == 2


def count_integers(lst):
    return sum(1 for item in lst if isinstance(item, int))

check(count_integers)