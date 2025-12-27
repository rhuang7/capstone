def check(candidate):
    assert candidate(35)==17
    assert candidate(7)==7
    assert candidate(100)==19


def max_digit_sum_split(n):
    if n < 2:
        return (n, 0)
    
    max_sum = 0
    best_split = (0, 0)
    
    for i in range(1, n):
        sum1 = sum(int(d) for d in str(i))
        sum2 = sum(int(d) for d in str(n - i))
        total_sum = sum1 + sum2
        
        if total_sum > max_sum:
            max_sum = total_sum
            best_split = (i, n - i)
    
    return best_split

check(max_digit_sum_split)