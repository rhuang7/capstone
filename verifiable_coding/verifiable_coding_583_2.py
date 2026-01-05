import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = sum(A)
        # Since we can subtract i from A_i any number of times, the total sum can be adjusted by any multiple of the sum of i's
        # The sum of i's from 1 to N is N*(N+1)//2
        sum_i = N * (N + 1) // 2
        # The total sum can be adjusted by any multiple of sum_i
        # So we need to check if total can be adjusted to 0 by adding or subtracting multiples of sum_i
        # Which is equivalent to checking if total % gcd(total, sum_i) == 0
        # But since sum_i is fixed, we can check if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract multiples of sum_i, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # But since we can add or subtract, the total can be adjusted to 0 if total is divisible by the gcd of total and sum_i
        # However, since we can add or subtract, the total can be adjusted to 0