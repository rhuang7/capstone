import sys
import math

MOD = 10**9 + 7

def is_lucky(n):
    s = str(n)
    for c in s:
        if c not in {'4', '7'}:
            return False
    return True

def count_lucky_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_lucky(i):
            count += 1
    return count

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        res = count_lucky_numbers(R) - count_lucky_numbers(L-1)
        results.append(res % MOD)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()