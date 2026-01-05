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
    for i in range(2, 10**6 + 1):
        if is_prime(i):
            primes_sum[i] = (primes_sum[i-1] + i) % 10
        else:
            primes_sum[i] = primes_sum[i-1]
    
    for n in cases:
        print(primes_sum[n])

if __name__ == '__main__':
    solve()