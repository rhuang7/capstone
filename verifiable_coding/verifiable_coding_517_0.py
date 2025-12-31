import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    # Precompute totient function for all numbers up to N
    max_n = N
    phi = list(range(max_n + 1))
    for i in range(2, max_n + 1):
        if phi[i] == i:
            for j in range(i, max_n + 1, i):
                phi[j] -= phi[j] // i
    
    # The number of non-periodic strings is equal to the sum of Euler's totient function for all divisors of N except N itself
    # Because a string of length N is non-periodic if and only if it cannot be written as v^n for some n >= 2
    # This is equivalent to the string having no proper period, which is counted by the sum of phi(d) for all d dividing N except N itself
    # So we need to find all divisors of N except N itself and sum phi(d)
    
    # Function to find all divisors of N
    def get_divisors(n):
        divisors = set()
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        divisors.discard(n)
        return sorted(divisors)
    
    divisors = get_divisors(N)
    total = 0
    for d in divisors:
        total += phi[d]
    
    print(total % M)

if __name__ == '__main__':
    solve()