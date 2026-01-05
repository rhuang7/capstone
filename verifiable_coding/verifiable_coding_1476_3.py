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
            if c in freq:
                freq[c] += 1
            else:
                freq[c] += 1
        
        total = len(s)
        denom = 1
        for count in freq.values():
            denom = denom * math.factorial(count) % MOD
        
        result = math.factorial(total) * pow(denom, MOD-2, MOD) % MOD
        print(result)

if __name__ == '__main__':
    solve()