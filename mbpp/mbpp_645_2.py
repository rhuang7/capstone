def check(candidate):
    assert candidate([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 665
    assert candidate([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 280
    assert candidate([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 0) == 210


def product_of_kth_index(tuples, k):
    product = 1
    for t in tuples:
        if len(t) > k:
            product *= t[k]
    return product

check(product_of_kth_index)