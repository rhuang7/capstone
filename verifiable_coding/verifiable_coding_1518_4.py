import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    # Precompute primes up to 1e5 using sieve of Eratosthenes
    max_n = 10**5
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    # Precompute possible sums of K primes
    # For each N and K, check if it can be formed by sum of K primes
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
        
        # Check if N - K is even and >= 2 (since K primes of 2 sum to 2*K)
        # Also, N - K must be >= 2 (so that we can have at least one more prime)
        if (N - K) >= 2 and (N - K) % 2 == 0:
            results.append('1')
        else:
            results.append('0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()