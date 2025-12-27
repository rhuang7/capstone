def check(candidate):
    assert candidate(9) == 5
    assert candidate(5) == 3
    assert candidate(11) == 6


def average_of_odds(n):
    if n % 2 == 0:
        raise ValueError("Input must be an odd number")
    
    # Number of odd numbers from 1 to n (inclusive)
    count = (n + 1) // 2
    
    # Sum of first m odd numbers is m^2
    sum_odds = count ** 2
    
    return sum_odds / count

check(average_of_odds)