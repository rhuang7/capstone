def check(candidate):
    assert candidate(1,5,2)==31
    assert candidate(1,5,4)==341
    assert candidate(2,6,3)==728


def geometric_progression_sum(first_term, common_ratio, number_of_terms):
    if number_of_terms == 0:
        return 0
    total = 0
    current = first_term
    for _ in range(number_of_terms):
        total += current
        current *= common_ratio
    return total

check(geometric_progression_sum)