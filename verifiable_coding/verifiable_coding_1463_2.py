import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        
        # Precompute smallest prime factors
        spf = list(range(N + 1))
        for i in range(2, int(N ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, N + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Group numbers by their prime factors
        groups = defaultdict(list)
        for i in range(1, N + 1):
            if i == 1:
                groups[1].append(i)
            else:
                factors = set()
                x = i
                while x > 1:
                    p = spf[x]
                    factors.add(p)
                    while x % p == 0:
                        x //= p
                groups[factors].append(i)
        
        # Assign numbers to days such that each day's pages are pairwise coprime
        days = []
        for group in groups.values():
            days.append(group)
        
        # Sort days by the number of pages in descending order
        days.sort(key=lambda x: -len(x))
        
        # Assign pages to days
        day_pages = []
        for day in days:
            day_pages.append(day)
        
        # Output the result
        D = len(day_pages)
        results.append(str(D))
        for day in day_pages:
            results.append(str(len(day)) + ' ' + ' '.join(map(str, day)))
    
    print('\n'.join(results))