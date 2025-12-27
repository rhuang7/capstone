def check(candidate):
    assert candidate(1,5,2)==25
    assert candidate(2,6,4)==72
    assert candidate(1,4,5)==34


def arithmetic_progression_sum(first_term, common_difference, number_of_terms):
    return (number_of_terms * (2 * first_term + (number_of_terms - 1) * common_difference)) // 2

check(arithmetic_progression_sum)