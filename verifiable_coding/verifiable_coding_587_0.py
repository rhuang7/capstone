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
    
    # For each girl, find the smallest possible boy strength such that XOR is prime
    # We'll use a frequency map for the girls' strengths
    freq = defaultdict(int)
    for s in girls:
        freq[s] += 1
    
    # We'll generate possible boy strengths and check if their XOR with a girl is prime
    # Since the maximum girl strength is 1e9, we can't generate all possible values
    # Instead, we'll use a set to store the required boy strengths
    
    boys = []
    for girl in girls:
        for i in range(1, 10**9 + 1):
            xor = girl ^ i
            if is_prime(xor):
                boys.append(i)
                break
    
    print(' '.join(map(str, boys)))

if __name__ == '__main__':
    solve()