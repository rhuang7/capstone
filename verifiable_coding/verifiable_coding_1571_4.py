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
        # Sum of AP = n/2 * (2a + (n-1)d) = total
        # => N/2 * (2A + (N-1)d) = total
        # => 2A + (N-1)d = 2 * total / N
        # => d = (2 * total / N - 2A) / (N - 1)
        
        numerator = 2 * total
        denominator = N
        d_numerator = numerator - 2 * A * denominator
        d_denominator = denominator * (N - 1)
        
        # Simplify d
        g = math.gcd(d_numerator, d_denominator)
        d_x = d_numerator // g
        d_y = d_denominator // g
        
        # K-th term of AP: a + (K-1)d
        # a = A, so term = A + (K-1) * d
        term_numerator = A * d_y + (K - 1) * d_x * d_y
        term_denominator = d_y
        
        # Simplify term
        g_term = math.gcd(term_numerator, term_denominator)
        X = term_numerator // g_term
        Y = term_denominator // g_term
        
        print(f"{X} {Y}")

if __name__ == '__main__':
    solve()