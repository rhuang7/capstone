import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        A = int(input[idx+1])
        K = int(input[idx+2])
        idx += 3
        
        # Sum of internal angles of a polygon
        total = (N - 2) * 180
        
        # The angles are in arithmetic progression
        # First term a = A, common difference d
        # Sum of arithmetic progression: S = N/2 * (2a + (N-1)d)
        # So, N/2 * (2A + (N-1)d) = total
        # Solve for d
        # 2A + (N-1)d = 2 * total / N
        # (N-1)d = (2 * total / N) - 2A
        # d = [(2 * total / N) - 2A] / (N-1)
        
        numerator = 2 * total - 2 * A * N
        denominator = N - 1
        
        # Simplify the fraction
        g = math.gcd(numerator, denominator)
        d = numerator // g
        e = denominator // g
        
        # K-th term of AP: a + (K-1)d
        X = A + (K - 1) * d
        Y = 1
        
        # Simplify X/Y
        g = math.gcd(X, Y)
        X = X // g
        Y = Y // g
        
        print(X, Y)

if __name__ == '__main__':
    solve()