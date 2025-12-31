import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute frequency of each number
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        # Compute all possible GCDs
        gcds = set()
        for num in A:
            current_gcd = num
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    gcds.add(i)
                    if num // i != i:
                        gcds.add(num // i)
        
        max_sum = 0
        # Try each possible GCD for B
        for g in gcds:
            # Check if there are at least two elements with this GCD
            count = 0
            for num in A:
                if num % g == 0:
                    count += 1
            if count >= 2:
                # Try to find the best GCD for C
                best_c = 0
                for num in A:
                    if num % g == 0:
                        continue
                    if num % best_c == 0:
                        best_c = num
                max_sum = max(max_sum, g + best_c)
        
        results.append(str(max_sum))
    
    print('\n'.join(results))