import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    mod = M
    
    # Precompute Euler's totient function for all numbers up to N
    phi = [0] * (N + 1)
    for i in range(1, N + 1):
        phi[i] = i
    for p in range(2, N + 1):
        if phi[p] == p:
            for multiple in range(p, N + 1, p):
                phi[multiple] -= phi[multiple] // p
    
    # Total number of strings of length N is 2^N
    total = pow(2, N, mod)
    
    # Subtract the number of periodic strings
    # A string is periodic if it can be written as v^n for some n >= 2
    # So, for each divisor d of N where d < N, we subtract the number of strings of length d that can be repeated
    # The number of such strings is phi(d)
    # So, the number of periodic strings is sum(phi(d) for d in divisors of N if d < N)
    
    # Find all divisors of N
    divisors = set()
    for i in range(2, N + 1):
        if N % i == 0:
            divisors.add(i)
    
    # Compute the sum of phi(d) for all divisors d of N where d < N
    sum_phi = 0
    for d in divisors:
        sum_phi += phi[d]
    
    # The answer is total - sum_phi
    answer = (total - sum_phi) % mod
    print(answer)

if __name__ == '__main__':
    solve()