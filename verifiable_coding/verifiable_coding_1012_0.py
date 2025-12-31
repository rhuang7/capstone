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

def char_value(c):
    return ord(c) - ord('a')

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    strings = input[1:T+1]

    for S in strings:
        n = len(S)
        prime_positions = [i for i in range(n) if is_prime(i+1)]
        prime_sum = 0
        for pos in prime_positions:
            prime_sum += char_value(S[pos])
        if is_prime(prime_sum):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()