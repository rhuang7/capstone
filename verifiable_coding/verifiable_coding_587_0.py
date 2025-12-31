import sys
import math
from collections import defaultdict

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(math.isqrt(x)) + 1
    for i in range(3, sqrt_x, 2):
        if x % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    girls = list(map(int, data[1:N+1]))
    
    # Precompute primes up to maximum possible XOR value (2^30)
    max_xor = 2**30
    sieve = [True] * (max_xor + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_xor)) + 1):
        if sieve[i]:
            for j in range(i*i, max_xor + 1, i):
                sieve[j] = False
    
    # For each girl, find the boy's strength that makes XOR a prime
    boys = []
    for girl in girls:
        for i in range(1, 2**30):
            if sieve[i ^ girl]:
                boys.append(i)
                break
    
    print(' '.join(map(str, boys)))

if __name__ == '__main__':
    solve()