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
        # First term is A, common difference is d
        # Sum of AP = N/2 * (2A + (N-1)d) = total
        # => 2A + (N-1)d = 2total / N
        # => d = (2total/N - 2A) / (N-1)
        
        numerator = 2 * total - 2 * A * N
        denominator = N * (N - 1)
        
        # Simplify the fraction for d
        gcd_val = math.gcd(numerator, denominator)
        d_num = numerator // gcd_val
        d_den = denominator // gcd_val
        
        # K-th term of AP is A + (K-1)d
        # So X = A + (K-1) * d_num / d_den
        # X = (A * d_den + (K-1) * d_num) / d_den
        numerator_k = A * d_den + (K - 1) * d_num
        denominator_k = d_den
        
        # Simplify the fraction for the K-th term
        gcd_k = math.gcd(numerator_k, denominator_k)
        X = numerator_k // gcd_k
        Y = denominator_k // gcd_k
        
        print(X, Y)

if __name__ == '__main__':
    solve()