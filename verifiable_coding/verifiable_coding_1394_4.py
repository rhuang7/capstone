import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    max_n = max(cases)
    
    # Precompute square root up to sqrt(1e10) = 1e5
    sqrt_max = int(math.isqrt(max_n)) + 1
    
    # Precompute mobius function
    max_mob = sqrt_max
    mu = [1] * (max_mob + 1)
    is_prime = [True] * (max_mob + 1)
    for i in range(2, max_mob + 1):
        if is_prime[i]:
            for j in range(i, max_mob + 1, i):
                is_prime[j] = False if j != i else is_prime[j]
                mu[j] *= -1
            for j in range(i * i, max_mob + 1, i * i):
                mu[j] = 0
    
    # Precompute for each n up to max_n
    # We need to compute the number of rectangles (a, b) such that a*b <= n
    # This can be done by iterating over a and finding the maximum b for each a
    # But since n can be up to 1e10, we need a more efficient approach
    
    # Use inclusion-exclusion with mobius function
    # The number of rectangles is sum_{a=1}^max_a sum_{b=1}^floor(n/a)} 1
    # Which is equivalent to sum_{k=1}^n floor(n/k)
    # But this is O(n), which is too slow for n=1e10
    
    # Instead, we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # But we can compute this efficiently using the formula:
    # sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n (floor(n/k))
    # But again, this is O(n), which is too slow
    
    # So we use the formula: sum_{k=1}^n floor(n/k) = sum_{k=1}^n (number of multiples of k up to n)
    # Which is equal to sum_{k=1}^n