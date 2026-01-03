import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for N in cases:
        total = N * N
        count = 0
        
        for b in range(1, N + 1):
            for a in range(1, N + 1):
                if math.gcd(a, b) == b:
                    count += 1
        
        gcd = math.gcd(count, total)
        print(f"{count//gcd}/{total//gcd}")

if __name__ == '__main__':
    solve()