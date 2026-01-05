import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for N in cases:
        if N == 1:
            print("1 1")
            continue
        
        total = 10 ** N
        same = 0
        
        if N % 2 == 0:
            half = N // 2
            same = 9 * 10 ** (half - 1)
        else:
            middle = N // 2
            same = 9 * 10 ** middle
        
        P = total - same
        Q = total
        
        g = math.gcd(P, Q)
        P //= g
        Q //= g
        
        print(f"{P} {Q}")

if __name__ == '__main__':
    solve()