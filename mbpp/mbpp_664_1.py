def check(candidate):
    assert candidate(2) == 2
    assert candidate(4) == 3
    assert candidate(100) == 51


def average_of_even_numbers(n):
    if n % 2 != 0:
        raise ValueError("Input must be an even number")
    
    # Sum of even numbers from 2 to n (inclusive)
    # Formula: sum = (number_of_terms) * (first_term + last_term) / 2
    number_of_terms = n // 2
    first_term = 2
    last_term = n
    total_sum = number_of_terms * (first_term + last_term) // 2
    
    # Average = total_sum / number_of_terms
    return total_sum / number_of_terms

check(average_of_even_numbers)