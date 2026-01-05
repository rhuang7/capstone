import sys
import math

MOD = 10**9 + 7

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def char_to_val(c):
    return ord(c) - ord('a')

def val_to_char(v):
    return chr(v + ord('a'))

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    strings = data[1:T+1]

    primes = [i for i in range(2, 100) if is_prime(i)]
    prime_positions = [i for i in range(len(primes))]

    for s in strings:
        n = len(s)
        prime_indices = [i for i in range(n) if is_prime(i+1)]
        total = 0
        for i in range(n):
            if is_prime(i+1):
                total += char_to_val(s[i])
        if is_prime(total):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()