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
        pages = list(range(1, N+1))
        days = []
        day_pages = []
        
        # Group pages by their prime factors
        prime_to_pages = defaultdict(list)
        for page in pages:
            if page == 1:
                continue
            factors = get_factors(page)
            for f in factors:
                prime_to_pages[f].append(page)
        
        # Assign pages to days based on their prime factors
        day_count = 0
        current_day = []
        for prime, pages_list in prime_to_pages.items():
            # Assign pages to the current day if possible
            if len(current_day) == 0:
                current_day = pages_list
            else:
                # Check if all primes in current_day are coprime with this prime
                can_add = True
                for p in prime_to_pages:
                    if p in prime_to_pages and p in prime_to_pages[prime]:
                        can_add = False
                        break
                if can_add:
                    current_day.extend(pages_list)
                else:
                    # Start a new day
                    day_count += 1
                    days.append(current_day)
                    current_day = pages_list
        if current_day:
            day_count += 1
            days.append(current_day)
        
        # Handle page 1 separately
        if 1 in pages:
            if not days:
                days.append([1])
            else:
                days[0].append(1)
        
        # Format the output
        result = []
        for i, day in enumerate(days, 1):
            result.append(f"{len(day)} {' '.join(map(str, day))}")
        return result
    
    for N in cases:
        output = solve_case(N)
        print(len(output))
        for line in output:
            print(line)

if __name__ == '__main__':
    solve()