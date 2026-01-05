import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    # Precompute primes up to 1e5 using Sieve of Eratosthenes
    max_n = 100000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # Edge cases
        if K == 1:
            if is_prime[N]:
                results.append('1')
            else:
                results.append('0')
            continue
        
        if N < K:
            results.append('0')
            continue
        
        # For K >= 2, check if N - (K-1) is >= 2 and is prime (since we need K primes)
        # Because the smallest K primes are 2, 2, ..., 2 (K times), sum is 2*K
        # So N must be >= 2*K and N - (K-1) must be >= 2 and prime
        if N < 2 * K:
            results.append('0')
            continue
        
        if is_prime[N - (K - 1)]:
            results.append('1')
        else:
            results.append('0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()