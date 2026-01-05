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
    
    # For each girl, find the smallest possible boy's strength such that XOR is prime
    # We'll use a sieve to precompute primes up to max possible XOR (which is up to 2*1e9)
    # But since XOR can be up to 2^30, we need a better approach
    
    # Instead, for each girl, try to find a boy's strength such that XOR is prime
    # We'll use a set to store all possible primes up to max XOR (which is up to 2*1e9)
    # But since N is up to 1e5, we need an efficient way
    
    # We'll use a set to store all primes up to max possible XOR
    max_xor = 0
    for a in girls:
        max_xor = max(max_xor, a)
    max_xor = 2 * max_xor
    
    # Generate all primes up to max_xor using sieve
    sieve = [True] * (max_xor + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_xor)) + 1):
        if sieve[i]:
            for j in range(i*i, max_xor + 1, i):
                sieve[j] = False
    
    primes = set(i for i, is_p in enumerate(sieve) if is_p)
    
    # For each girl, find the smallest possible boy's strength such that XOR is prime
    # We'll use a set to store all possible boy strengths
    boys = set()
    for a in girls:
        for b in boys:
            if (a ^ b) in primes:
                print(b, end=' ')
                break
        else:
            # If not found, add a new boy strength
            # We'll use a value that ensures XOR is prime
            # Try to find the smallest possible value
            for b in range(1, 1000000):
                if (a ^ b) in primes:
                    print(b, end=' ')
                    break
            else:
                # If not found, use a default value
                print(a + 1, end=' ')
    
    print()

if __name__ == '__main__':
    solve()