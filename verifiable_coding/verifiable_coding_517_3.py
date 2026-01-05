import sys

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
    
    # The number of non-periodic strings is equal to the sum of Euler's totient function for all divisors of N greater than 1
    # Because a string of length N is non-periodic if it cannot be written as v^n for some n >= 2
    # This is equivalent to saying that the string has no proper divisor d of N such that the string is periodic with period d
    # So we sum phi(d) for all d dividing N, d > 1
    
    # Find all divisors of N
    divisors = set()
    for i in range(2, N + 1):
        if N % i == 0:
            divisors.add(i)
    
    result = 0
    for d in divisors:
        result += phi[d]
    
    print(result % mod)

if __name__ == '__main__':
    solve()