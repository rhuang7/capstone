import sys
import math
from math import gcd
from functools import reduce

def compute_gcd_list(numbers):
    return reduce(math.gcd, numbers)

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
        S = data[idx]
        idx += 1
        M, X, Y = map(int, data[idx:idx+3])
        idx += 3
        
        # Precompute all possible numbers with up to M digits
        possible_numbers = []
        for i in range(1, M+1):
            for j in range(N - i + 1):
                num_str = S[j:j+i]
                if len(num_str) > 0:
                    possible_numbers.append(int(num_str))
        
        # Try all possible GCD values
        max_gcd = 0
        for candidate in possible_numbers:
            # Check if we can split the string into parts with this candidate as GCD
            # We need to split the string into parts where each part is divisible by candidate
            # And we need to use at least X and at most Y separators
            # We can use binary search for this
            # We'll try to find the maximum number of parts we can split into with this candidate
            # and check if it's possible to use between X and Y separators
            # We'll use a greedy approach to split the string into parts
            # We'll try to split as much as possible
            parts = []
            current = 0
            count = 0
            for i in range(N):
                current = current * 10 + int(S[i])
                if current % candidate == 0:
                    parts.append(current)
                    current = 0
                    count += 1
            if count >= 1 and count <= N:
                # We can split into count parts
                # The number of separators is count - 1
                if X <= (count - 1) <= Y:
                    max_gcd = max(max_gcd, candidate)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()