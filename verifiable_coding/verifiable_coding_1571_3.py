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
        # So, (N/2) * (2A + (N-1)d) = total
        # => 2A + (N-1)d = 2 * total / N
        # => (N-1)d = (2 * total / N) - 2A
        # => d = [(2 * total / N) - 2A] / (N-1)
        
        # Calculate d
        numerator = 2 * total - 2 * A * N
        denominator = N * (N - 1)
        d = numerator / denominator
        
        # K-th term of AP is a + (K-1)d
        # So, X = A + (K-1)*d
        # Y = 1 (since d is rational, but we need to represent it as a fraction)
        
        # Since d is rational, we can represent it as a fraction
        # But since we are using floating point, we need to compute it as a fraction
        # Let's compute X as a fraction
        
        # X = A + (K-1) * d
        # d = (2 * total / N - 2A) / (N-1)
        # So X = A + (K-1) * (2 * total / N - 2A) / (N-1)
        
        # Let's compute it as a fraction
        # X = [A * (N-1) + (K-1) * (2 * total - 2A * N)] / (N-1)
        
        numerator_x = A * (N - 1) + (K - 1) * (2 * total - 2 * A * N)
        denominator_x = N - 1
        
        # Simplify the fraction
        gcd_val = math.gcd(numerator_x, denominator_x)
        X = numerator_x // gcd_val
        Y = denominator_x // gcd_val
        
        print(f"{X} {Y}")

if __name__ == '__main__':
    solve()