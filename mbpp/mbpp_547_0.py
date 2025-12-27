def check(candidate):
    assert candidate(4) == 7
    assert candidate(2) == 3
    assert candidate(5) == 8


def sum_hamming_distances(n):
    def count_hamming_distance(a, b):
        return bin(a ^ b).count('1')
    
    total = 0
    for i in range(n + 1):
        total += count_hamming_distance(i, i + 1)
    return total

check(sum_hamming_distances)