def check(candidate):
    assert candidate(2,2) == 2
    assert candidate(2,5) == 2
    assert candidate(5,10) == 2


def max_occuring_divisor(nums):
    from collections import defaultdict

    count = defaultdict(int)
    max_count = 0
    max_divisor = 1

    for num in nums:
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count[i] += 1
                if num // i != i:
                    count[num // i] += 1
        if count[num] > max_count:
            max_count = count[num]
            max_divisor = num
        elif count[num] == max_count and num > max_divisor:
            max_divisor = num

    return max_divisor

check(max_occuring_divisor)