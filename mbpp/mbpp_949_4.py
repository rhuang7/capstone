def check(candidate):
    assert candidate([(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)] ) == '[(1, 2), (12345,), (3, 4, 6, 723), (134, 234, 34)]'
    assert candidate([(3, 4, 8), (1, 2), (1234335,), (1345, 234, 334)] ) == '[(1, 2), (3, 4, 8), (1234335,), (1345, 234, 334)]'
    assert candidate([(34, 4, 61, 723), (1, 2), (145,), (134, 23)] ) == '[(1, 2), (145,), (134, 23), (34, 4, 61, 723)]'


def sort_by_total_digits(tuples_list):
    def digit_sum(t):
        return sum(int(d) for d in str(t))
    
    return sorted(tuples_list, key=digit_sum)

check(sort_by_total_digits)