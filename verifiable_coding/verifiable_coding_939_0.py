import sys
import math

MOD = 10**9 + 7

def is_lucky(n):
    return all(c in '47' for c in str(n))

def count_lucky_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_lucky(i):
            count += 1
    return count

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        L = int(input[idx])
        R = int(input[idx+1])
        idx += 2
        result = count_lucky_numbers(R) - count_lucky_numbers(L - 1)
        print(result % MOD)

if __name__ == '__main__':
    solve()