def check(candidate):
    assert candidate(12) == 13
    assert candidate(24) == 27
    assert candidate(23) == 23


def max_sum_three_parts(n):
    if n < 3:
        return 0  # Cannot split into three parts if n < 3
    
    # Base case: when n is exactly 3, the maximum sum is 1 + 1 + 1 = 3
    if n == 3:
        return 3
    
    # Recursive case: try all possible splits into three parts
    max_total = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            current_sum = max_sum_three_parts(i) + max_sum_three_parts(j) + max_sum_three_parts(n - i - j)
            if current_sum > max_total:
                max_total = current_sum
    return max_total

check(max_sum_three_parts)