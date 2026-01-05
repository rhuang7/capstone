import sys

def solve():
    import math
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
        # So we need exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which means N_slots must have exactly one divisor in that range
        # Which implies that N_slots is a prime number, because primes have only 1 and themselves as divisors
        # But since the first and last slots are occupied, the divisor can't be N_slots itself
        # So the only possible divisor is 1, which is always present
        # So we need to check if N_slots is a prime number
        # But wait, if N_slots is 4, then the empty slots are 2, which divides 4
        # So we need to check if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which is equivalent to checking if N_slots is a prime number
        # Because if N_slots is a prime, then the only divisors are 1 and N_slots
        # But since N_slots is the total number of slots, the divisor can't be N_slots
        # So the only possible divisor is 1, which is in the range [1, N_slots-2]
        # So the answer is YES if N_slots is a prime number
        # But wait, what about N_slots = 4? The empty slots are 2, which divides 4
        # So 4 is not a prime, but it still has exactly one divisor in the range [1, N_slots-2]
        # So the previous reasoning is incorrect
        # We need to find if there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which means the number of divisors of N_slots in that range is exactly 1
        # So we need to check if the number of divisors of N_slots in that range is exactly 1
        # Which is equivalent to checking if N_slots is a prime number or a square of a prime
        # Because for a prime p, the only divisors are 1 and p
        # But since p is the total number of slots, the divisor can't be p
        # So the only possible divisor is 1, which is in the range [1, N_slots-2]
        # For a square of a prime, say p^2, the divisors are 1, p, and p^2
        # But since p^2 is the total number of slots, the divisor can't be p^2
        # So the only possible divisors in the range are 1 and p
        # But we need exactly one divisor, so p must be 1, which is not possible
        # So the only valid case is when N_slots is a prime number
        # So the correct condition is that N_slots is a prime number
        # But wait, what about N_slots = 6? The empty slots are 2, 3, 4
        # The divisors of 6 are 1, 2, 3, 6
        # The divisors in the range [1, 4] are 1, 2, 3
        # So there are three divisors, which is more than one
        # So the answer is NO
        # So the correct condition is that N_slots is a prime number
        # So we need to check if N_slots is a prime number
        # But what about N_slots = 4? The empty slots are 2, which divides 4
        # So the answer is YES
        # So the previous reasoning is incorrect
        # So the correct condition is that there is exactly one divisor of N_slots in the range [1, N_slots-2]
        # Which means that the number of divisors of N_slots in that range is exactly 1
        # So we need to find if there is exactly one divisor of N_slots in that range
        # So we can iterate through all possible divisors of N_slots up to sqrt(N_slots)
        # And count how many of them are in the range [1, N_slots-2]
        # If the count is exactly 1, then output YES, else NO
        # So the correct approach is to find the number of divisors of N_slots in the range [1, N_slots-2]
        # And check if it is exactly 1
        # So we can do the following:
        # 1. Check if N_slots is less than 2: if so, output NO
        # 2. Else, iterate from 1 to sqrt(N_slots)
        # 3. For each i that divides N_slots, check if i is in the range [1, N_slots-2]
        # 4. Also check if N_slots / i is in the range [1, N_slots-2]
        # 5. Count the total number of such divisors
        # 6. If the count is exactly 1, output YES, else NO
        # So let's implement this
        # Edge case: N_slots = 2
        if N_slots == 2:
            print("NO")
            continue
        # Initialize count
        count = 0
        # Iterate from 1 to sqrt(N_slots)
        for i in range(1, int(math.isqrt(N_slots)) + 1):
            if N_slots % i == 0:
                # Check if i is in the range [1, N_slots-2]
                if 1 <= i <= N_slots - 2:
                    count += 1
                # Check if N_slots / i is in the range [1, N_slots-2]
                if i != N_slots // i and 1 <= N_slots // i <= N_slots - 2:
                    count += 1
        if count == 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()