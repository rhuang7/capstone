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
    
    primes_sum = [0] * (10**6 + 1)
    prime = 2
    while prime <= 10**6:
        primes_sum[prime] = primes_sum[prime - 1] + prime
        for i in range(prime * 2, 10**6 + 1, prime):
            primes_sum[i] = primes_sum[i - 1] + prime
        prime = primes_sum.index(prime + 1, prime + 1) + 1
    
    for n in cases:
        print(primes_sum[n] % 10)

if __name__ == '__main__':
    solve()