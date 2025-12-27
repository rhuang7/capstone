def check(candidate):
    assert candidate([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
    assert candidate([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == '[(5, 25, 30)]'
    assert candidate([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'


def find_divisible_tuples(tuples_list, k):
    return [tpl for tpl in tuples_list if all(num % k == 0 for num in tpl)]

check(find_divisible_tuples)