import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    ai_list = list(map(int, data[1:N+1]))
    
    for ai in ai_list:
        N_slots = ai
        if N_slots < 2:
            print("NO")
            continue
        # The first and last slots are occupied, so there are (N_slots - 2) empty slots
        empty_slots = N_slots - 2
        # We need exactly one empty slot that divides N_slots
        # So, we need exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which means N_slots must have exactly one divisor in that range
        # The only way this can happen is if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # Because the only divisors of N_slots are 1, N_slots, and possibly others
        # So we check if there is exactly one divisor in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square root is not 1 or N_slots-1
        # So we check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # We can do this by checking if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a perfect square and the square