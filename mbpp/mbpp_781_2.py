def check(candidate):
    assert candidate(10) == "Even"
    assert candidate(100) == "Odd"
    assert candidate(125) == "Even"


def is_divisor_count_even_or_odd(n):
    if n <= 0:
        return "Invalid input: n must be a positive integer"
    
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    
    return "even" if count % 2 == 0 else "odd"

check(is_divisor_count_even_or_odd)