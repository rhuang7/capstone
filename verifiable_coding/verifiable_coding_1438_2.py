import sys
import math
from collections import defaultdict

def sieve(max_limit):
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, max_limit + 1, i):
                is_prime[j] = False
    return is_prime

def get_prime_factors(x, is_prime):
    factors = set()
    while x > 1:
        for i in range(2, int(math.sqrt(x)) + 1):
            if is_prime[i] and x % i == 0:
                factors.add(i)
                while x % i == 0:
                    x //= i
                break
        else:
            if is_prime[x]:
                factors.add(x)
            break
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    max_a = 0
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        max_a = max(max_a, max(a))
    is_prime = sieve(max_a)
    prime_sum = dict()
    for x in a:
        factors = get_prime_factors(x, is_prime)
        s = sum(factors)
        prime_sum[x] = s
    count = defaultdict(int)
    for x in a:
        count[prime_sum[x]] += 1
    res = 0
    for key in count:
        c = count[key]
        res += c * (c - 1)
    print(res)

if __name__ == '__main__':
    solve()