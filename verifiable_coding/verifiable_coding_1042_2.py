import sys
import math

def solve():
    import sys
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
        coprime_count = 0
        for i in range(1, N+1):
            is_coprime = True
            for p in primes:
                if i % p == 0:
                    is_coprime = False
                    break
            if is_coprime:
                coprime_count += 1
        
        # Calculate the number of good pairs
        good_pairs = (coprime_count * (coprime_count - 1)) // 2
        results.append(good_pairs)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()