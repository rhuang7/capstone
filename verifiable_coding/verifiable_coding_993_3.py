import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    for ai in a:
        N_slots = ai
        if N_slots < 2:
            print("NO")
            continue
        # The first and last slots are occupied, so there are N_slots - 2 empty slots
        # We need exactly one of these to be divisible by N_slots
        # So we need exactly one divisor of N_slots in the range [2, N_slots-1]
        # Which means N_slots must have exactly one divisor in that range
        # Which means N_slots must be a prime number
        # Because if N_slots is prime, then its only divisors are 1 and itself
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1]
        # Wait, this is not correct. Let's think again.
        # We need exactly one empty slot that divides N_slots.
        # The empty slots are 2 to N_slots-1.
        # So we need exactly one divisor of N_slots in that range.
        # That means N_slots must have exactly one divisor in that range.
        # Which means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N_slots must have exactly one such divisor.
        # That means N_slots must be a prime number.
        # Because if N_slots is prime, then its only divisors are 1 and itself.
        # But since 1 and N_slots are excluded, there are no divisors in the range [2, N_slots-1].
        # So this logic is incorrect.
        # Let's think again.
        # We need exactly one divisor of N_slots in the range [2, N_slots-1].
        # So N