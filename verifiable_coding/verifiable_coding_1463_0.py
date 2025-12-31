import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.isqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    def get_primes_up_to(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.isqrt(n)) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        primes = [i for i, val in enumerate(sieve) if val]
        return primes
    
    def factorize(x):
        factors = []
        i = 2
        while i * i <= x:
            if x % i == 0:
                factors.append(i)
                while x % i == 0:
                    x //= i
            i += 1
        if x > 1:
            factors.append(x)
        return factors
    
    def group_pages(n):
        primes = get_primes_up_to(n)
        prime_to_group = defaultdict(list)
        for i in range(1, n+1):
            if i == 1:
                prime_to_group[1].append(i)
            else:
                factors = factorize(i)
                if factors:
                    prime = factors[0]
                    prime_to_group[prime].append(i)
                else:
                    prime_to_group[1].append(i)
        
        groups = []
        for prime in sorted(prime_to_group.keys()):
            groups.append(prime_to_group[prime])
        
        days = []
        current_day = []
        for group in groups:
            if not current_day:
                current_day = group
            else:
                valid = True
                for num in current_day:
                    for p in factorize(num):
                        if p in [f for f in factorize(x) for x in group]:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    current_day += group
                else:
                    days.append(current_day)
                    current_day = group
        if current_day:
            days.append(current_day)
        
        return days
    
    for n in cases:
        days = group_pages(n)
        print(len(days))
        for day in days:
            print(len(day), end=' ')
            print(' '.join(map(str, day)))
    
if __name__ == '__main__':
    solve()