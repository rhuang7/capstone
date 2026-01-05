import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        total = len(s)
        result = math.factorial(total)
        for count in freq.values():
            result //= math.factorial(count)
        print(result % MOD)

if __name__ == '__main__':
    solve()