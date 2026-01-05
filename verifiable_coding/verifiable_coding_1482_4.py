import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N == 1:
            print("1 1")
            continue
        
        total = 10 ** N
        same = 0
        
        if N % 2 == 0:
            half = N // 2
            same = 9 * (10 ** (half - 1))
        else:
            mid = N // 2
            same = 9 * (10 ** mid)
        
        prob = same / total
        p = same
        q = total
        
        gcd_val = math.gcd(p, q)
        p //= gcd_val
        q //= gcd_val
        
        print(f"{p} {q}")

if __name__ == '__main__':
    solve()