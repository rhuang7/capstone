import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    for ai in a:
        N_slots = ai
        # The first and last slots are occupied, so available slots are N_slots - 2
        available = N_slots - 2
        # We need exactly one empty slot that divides N_slots
        # So, we need exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which means, the number of divisors of N_slots in [1, N_slots-2] must be exactly 1
        # The only way this can happen is if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # Because the square root is the only divisor that divides N_slots and is in the range
        # Also, the square root must not be 1 or N_slots-1, because those are already occupied
        # So, check if N_slots is a perfect square and sqrt(N_slots) is not 1 or N_slots-1
        sqrt_n = int(math.isqrt(N_slots))
        if sqrt_n * sqrt_n == N_slots and sqrt_n != 1 and sqrt_n != N_slots - 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()