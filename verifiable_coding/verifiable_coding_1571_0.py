import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        A = int(data[index+1])
        K = int(data[index+2])
        index += 3
        
        # Sum of internal angles of a polygon
        total = (N - 2) * 180
        
        # Common difference of the arithmetic progression
        d = (total - N * A) // N
        
        # K-th angle in AP
        X = A + (K - 1) * d
        Y = 1
        
        # Output as X/Y with gcd(X, Y) = 1
        print(f"{X} {Y}")

if __name__ == '__main__':
    solve()