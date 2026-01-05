import sys
import math
from collections import defaultdict

def sieve(max_limit):
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_limit + 1, i):
                is_prime[j] = False
    return is_prime

def get_s(x, is_prime):
    s = 0
    while x > 1:
        for p in range(2, x + 1):
            if is_prime[p] and x % p == 0:
                s += p
                while x % p == 0:
                    x //= p
                break
    return s

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
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        s_dict = defaultdict(int)
        for num in a:
            s = get_s(num, is_prime)
            s_dict[s] += 1
        count = 0
        for s1, cnt1 in s_dict.items():
            for s2, cnt2 in s_dict.items():
                if s1 != 0 and s2 % s1 == 0:
                    count += cnt1 * cnt2
        print(count)

if __name__ == '__main__':
    solve()