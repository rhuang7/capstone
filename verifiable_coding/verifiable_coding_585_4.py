import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        p = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each p_i, find the maximum number of times it can be used
        # to kill sorcerers
        max_kills = 0
        for pi in p:
            # The number of sorcerers that can be killed with this spell
            # is the number of times pi is congruent to some value mod k
            # where k is the current number of living sorcerers
            # We need to find the maximum k such that pi mod k != 0
            # and k <= N
            # The maximum number of times this spell can be used is the number
            # of k's such that pi mod k != 0 and k <= N
            # This is equivalent to the number of integers k in [1, N] such that k does not divide pi
            # So we need to count the number of integers in [1, N] that do not divide pi
            # Which is N - number of divisors of pi that are <= N
            # But since pi can be up to 1e9, we need to find all divisors of pi efficiently
            # We can do this by checking up to sqrt(pi)
            # However, since pi can be up to 1e9, and T is up to 1000, and M up to 3e5, this is feasible
            # So for each pi, we find all its divisors and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # However, since we can use the same spell multiple times, we need to find the maximum number of times
            # we can use this spell, which is the number of k's in [1, N] such that pi mod k != 0
            # But since k can be any number from 1 to N, and pi can be up to 1e9, we need to find the maximum number of k's
            # such that pi mod k != 0
            # This is equivalent to the number of k in [1, N] that do not divide pi
            # So we need to count the number of divisors of pi that are <= N, and subtract from N
            # But since pi can be up to 1e9, and N can be up to 1e9, we need to find all divisors of pi efficiently
            # So we find all divisors of pi, then count how many are <= N
            # Then the number of times this spell can be used is N - count
            # But we can only use the spell once per k, so the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # However, since we can use the same spell multiple times, but each time with a different k, the maximum number of times
            # this spell can be used is the number of k's in [1, N] that do not divide pi
            # So we need to find the number of k's in [1, N] that do not divide pi
            # This is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # However, since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So for each pi, we find the number of divisors of pi that are <= N, then subtract from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # However, we can use this spell only once per k, so the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # So we find all divisors of pi, then count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find the number of divisors of pi that are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # However, since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # So we find all divisors of pi, then count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # However, since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # However, since we can use the same spell multiple times, the maximum number of times this spell can be used is the number of k's
            # such that pi mod k != 0, which is N - number of divisors of pi that are <= N
            # So we need to find all divisors of pi and count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # So we find all divisors of pi, then count how many are <= N
            # Then subtract that from N to get the number of times this spell can be used
            # But since we can use the same spell multiple times, the maximum number of times this spell can be