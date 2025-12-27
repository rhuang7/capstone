def check(candidate):
    assert candidate(5) == 3
    assert candidate(10) == 5
    assert candidate(15) == 8


def count_odd_set_bits_numbers(n):
    def count_set_bits(x):
        return bin(x).count('1')
    
    count = 0
    for i in range(n + 1):
        if count_set_bits(i) % 2 == 1:
            count += 1
    return count

check(count_odd_set_bits_numbers)