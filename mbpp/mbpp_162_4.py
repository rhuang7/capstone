def check(candidate):
    assert candidate(6)==12
    assert candidate(10)==30
    assert candidate(9)==25


def sum_positive_arithmetic_series(n):
    if n <= 0:
        return 0
    # Calculate the number of terms in the series
    terms = (n // 2) + 1
    # Sum of arithmetic series: (number_of_terms * (first_term + last_term)) // 2
    return (terms * (n + (n - 2 * (terms - 1)))) // 2

check(sum_positive_arithmetic_series)