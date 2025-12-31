import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for N in cases:
        total = N * N
        count = 0
        
        for b in range(1, N+1):
            for a in range(1, N+1):
                if math.gcd(a, b) == b:
                    count += 1
        
        gcd_count = 0
        for b in range(1, N+1):
            for a in range(1, N+1):
                if math.gcd(a, b) == b:
                    gcd_count += 1
        
        numerator = gcd_count
        denominator = total
        
        g = math.gcd(numerator, denominator)
        numerator //= g
        denominator //= g
        
        print(f"{numerator}/{denominator}")

if __name__ == '__main__':
    solve()