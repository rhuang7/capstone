import sys
import math
from collections import defaultdict

def solve():
    import sys
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
    
    def get_prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def solve_case(N):
        if N == 0:
            return []
        prime_factors = defaultdict(list)
        for i in range(1, N + 1):
            if i == 1:
                continue
            if is_prime(i):
                prime_factors[i].append(i)
            else:
                factors = get_prime_factors(i)
                for p in factors:
                    prime_factors[p].append(i)
        
        days = []
        current_day = []
        for i in range(1, N + 1):
            if i == 1:
                current_day.append(i)
                days.append(current_day)
                current_day = []
                continue
            if len(current_day) == 0:
                current_day.append(i)
                days.append(current_day)
                current_day = []
            else:
                can_add = True
                for page in current_day:
                    if not math.gcd(page, i) == 1:
                        can_add = False
                        break
                if can_add:
                    current_day.append(i)
                else:
                    days.append([i])
                    current_day = [i]
        return days
    
    results = []
    for N in cases:
        days = solve_case(N)
        results.append(len(days))
        for day in days:
            results.append(str(len(day)) + ' ' + ' '.join(map(str, day)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()