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
        
        total = 1
        for count in freq.values():
            total = total * math.factorial(count) % MOD
        
        print(total)

if __name__ == '__main__':
    solve()