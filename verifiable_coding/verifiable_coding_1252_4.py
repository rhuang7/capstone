import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    cases = list(map(int, input[1:t+1]))
    
    # Precompute primes up to 1e6 and their cumulative sum
    max_n = max(cases)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False
    # Compute cumulative sum of primes
    cum_sum = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        cum_sum[i] = cum_sum[i-1] + (i if sieve[i] else 0)
    
    for n in cases:
        print(cum_sum[n] % 10)

if __name__ == '__main__':
    solve()