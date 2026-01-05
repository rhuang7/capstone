import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_primes_up_to(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.isqrt(n)) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        primes = [i for i, is_p in enumerate(sieve) if is_p]
        return primes
    
    def factorize(n):
        factors = {}
        while n % 2 == 0:
            factors[2] = True
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors[i] = True
                n //= i
            i += 2
        if n > 1:
            factors[n] = True
        return factors
    
    def group_pages(n):
        primes = get_primes_up_to(n)
        prime_to_group = {}
        for p in primes:
            prime_to_group[p] = []
        for i in range(1, n + 1):
            if i == 1:
                continue
            factors = factorize(i)
            for p in factors:
                prime_to_group[p].append(i)
        
        groups = []
        for p in primes:
            if prime_to_group[p]:
                groups.append(prime_to_group[p])
        
        days = []
        current_day = []
        for i in range(1, n + 1):
            if i == 1:
                current_day.append(i)
            else:
                assigned = False
                for g in groups:
                    if i in g:
                        current_day.append(i)
                        assigned = True
                        break
                if not assigned:
                    days.append(current_day)
                    current_day = [i]
        if current_day:
            days.append(current_day)
        
        return days
    
    results = []
    for N in cases:
        days = group_pages(N)
        results.append(len(days))
        for day in days:
            results.append(str(len(day)) + ' ' + ' '.join(map(str, day)))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()