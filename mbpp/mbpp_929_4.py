def check(candidate):
    assert candidate((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3
    assert candidate((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2
    assert candidate((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4


def count_repeated_items(tup):
    from collections import Counter
    return dict(Counter(tup))

check(count_repeated_items)