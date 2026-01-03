import sys
import math
from collections import defaultdict

def get_prime_factors(x):
    factors = set()
    while x % 2 == 0:
        factors.add(2)
        x //= 2
    i = 3
    while i * i <= x:
        while x % i == 0:
            factors.add(i)
            x //= i
        i += 2
    if x > 1:
        factors.add(x)
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    S = int(data[2])
    arr = list(map(int, data[3:3+N]))
    
    max_sum = -float('inf')
    
    for i in range(N):
        current_sum = 0
        current_factors = set()
        for j in range(i, N):
            current_sum += arr[j]
            factors = get_prime_factors(arr[j])
            current_factors.update(factors)
            p = len(current_factors)
            special_sum = current_sum * (K - p * S)
            if special_sum > max_sum:
                max_sum = special_sum
    print(max_sum)

if __name__ == '__main__':
    solve()