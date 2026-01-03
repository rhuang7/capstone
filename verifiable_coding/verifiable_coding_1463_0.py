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
    
    def get_factors(n):
        factors = set()
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                factors.add(i)
                if n // i != i:
                    factors.add(n // i)
        if n > 1:
            factors.add(n)
        return factors
    
    def solve_case(N):
        if N == 0:
            return []
        pages = list(range(1, N + 1))
        days = []
        current_day = []
        for page in pages:
            if page == 1:
                current_day.append(page)
                continue
            can_add = True
            for p in current_day:
                if math.gcd(page, p) != 1:
                    can_add = False
                    break
            if can_add:
                current_day.append(page)
            else:
                days.append(current_day)
                current_day = [page]
        if current_day:
            days.append(current_day)
        return days
    
    results = []
    for N in cases:
        days = solve_case(N)
        results.append(len(days))
        for day in days:
            results.append(str(len(day)) + ' ' + ' '.join(map(str, day)))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()