import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        unique_chars = set(s)
        n = len(s)
        total = math.factorial(n)
        for c in unique_chars:
            count = s.count(c)
            total = total // math.factorial(count)
        print(total % MOD)

if __name__ == '__main__':
    solve()