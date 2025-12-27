def check(candidate):
    assert candidate((5, 6, 3, 6, 10, 34)) == (46, 18)
    assert candidate((1, 2, 3, 4, 5)) == (6, 9)
    assert candidate((6, 7, 8, 9, 4, 5)) == (21, 18)


def sum_alternate_chains(tuples_list):
    if not tuples_list:
        return 0
    
    total = 0
    for i, tup in enumerate(tuples_list):
        if i % 2 == 0:
            total += sum(tup)
    return total

check(sum_alternate_chains)