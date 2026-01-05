import sys
import math
from collections import defaultdict

def get_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
    if n > 1:
        factors.add(n)
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    S = int(data[2])
    arr = list(map(int, data[3:3+N]))
    
    max_special_sum = -float('inf')
    
    for i in range(N):
        current_sum = 0
        current_product = 1
        prime_factors = set()
        for j in range(i, N):
            current_sum += arr[j]
            current_product *= arr[j]
            factors = get_prime_factors(arr[j])
            prime_factors.update(factors)
            p = len(prime_factors)
            special_sum = current_sum * (K - p * S)
            if special_sum > max_special_sum:
                max_special_sum = special_sum
    
    print(max_special_sum)

if __name__ == '__main__':
    solve()