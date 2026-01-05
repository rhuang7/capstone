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
    
    # For each girl, find a boy's strength such that XOR is prime
    # We need to find for each girl a value that when XORed with her strength is prime
    # We'll try to find the minimal sum of primes, but since each girl must pair with a unique boy, we need to find a permutation of boys' strengths such that XOR with each girl is prime
    
    # Since we need to find the minimal sum, we can try to find for each girl the smallest possible value that when XORed with her strength is prime
    # However, since each boy must be used exactly once, we need to find a permutation of values that satisfies this condition
    
    # We'll try to find for each girl the smallest possible value that when XORed with her strength is prime, and then check if the values are unique
    # If not, we'll try the next possible value
    
    # We'll use a greedy approach to find the minimal sum
    # We'll try to find for each girl the smallest possible value that when XORed with her strength is prime, and that hasn't been used yet
    
    # We'll use a set to track used values
    used = set()
    result = []
    
    for girl in girls:
        found = False
        # Try values starting from 1
        for val in range(1, 10**9):
            if val in used:
                continue
            hate = girl ^ val
            if is_prime(hate):
                result.append(val)
                used.add(val)
                found = True
                break
        if not found:
            # This should not happen as per problem statement
            pass
    
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()