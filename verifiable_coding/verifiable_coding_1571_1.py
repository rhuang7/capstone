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
        
        # The angles are in arithmetic progression
        # First term a = A, common difference d
        # Sum of AP = (N/2) * (2a + (N-1)d) = total
        # => (N/2) * (2A + (N-1)d) = total
        # => 2A + (N-1)d = 2*total/N
        # => d = (2*total/N - 2A) / (N-1)
        
        numerator = 2 * total
        denominator = N
        term = numerator // denominator
        d = (term - 2 * A) // (N - 1)
        
        # K-th term of AP: a + (K-1)d
        X = A + (K - 1) * d
        Y = 1
        
        # Simplify X/Y
        gcd_val = math.gcd(X, Y)
        X //= gcd_val
        Y //= gcd_val
        
        print(X, Y)

if __name__ == '__main__':
    solve()