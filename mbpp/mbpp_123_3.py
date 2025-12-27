def check(candidate):
    assert candidate(999)==504
    assert candidate(9999)==31626
    assert candidate(99)==0


def sum_amicable_numbers(limit):
    def is_perfect(n):
        return sum(i for i in range(1, n) if n % i == 0) == n

    def is_amicable(a, b):
        return is_perfect(a) and is_perfect(b) and a != b

    amicable_sum = 0
    seen = set()
    
    for i in range(2, limit + 1):
        if i in seen:
            continue
        j = sum(i for i in range(1, i) if i % i == 0)
        if j > limit:
            continue
        if is_amicable(i, j):
            amicable_sum += i + j
            seen.add(i)
            seen.add(j)
    
    return amicable_sum

check(sum_amicable_numbers)