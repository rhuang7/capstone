import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = int(data[index+1])
        index += 2
        
        # Find all primes in P
        primes = set()
        temp = P
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                primes.add(i)
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            primes.add(temp)
        
        # Count numbers in [1, N] that are coprime with P
        count = 0
        for i in range(1, N+1):
            is_coprime = True
            for p in primes:
                if i % p == 0:
                    is_coprime = False
                    break
            if is_coprime:
                count += 1
        
        # Count good pairs (a, b) with a < b and both coprime with P
        good_pairs = 0
        for i in range(1, N+1):
            if i % 2 == 1:  # Only consider odd indices to avoid duplicates
                for j in range(i+1, N+1):
                    if j % 2 == 1:  # Only consider odd indices
                        if i % 2 == 1 and j % 2 == 1:
                            good_pairs += 1
        
        results.append(good_pairs)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()