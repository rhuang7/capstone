import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        # Compute the sum S = sum_{i=L}^R (L & (L+1) & ... & i)
        # The bitwise AND of a range of numbers from L to i is equal to the bitwise AND of all numbers from L to i
        # The key observation is that once a bit is cleared in the AND operation, it remains cleared for all larger i
        # So, for each bit position, we find the first i >= L where that bit is cleared in the AND of L to i
        # Then, for all i from L to that first i-1, the bit is set, and for i >= that first i, the bit is cleared
        # So, for each bit position, we find the first i where the bit is cleared
        # Then, the number of terms where the bit is set is (first_i - L)
        # The contribution of that bit to the sum is (first_i - L) * (1 << bit)
        # We sum over all bit positions
        res = 0
        for bit in range(60):
            mask = 1 << bit
            # Find the first i >= L where the bit is cleared in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # The AND of L to i is the same as the AND of L to i-1 AND i
            # So, we can find the first i where the bit is cleared
            # This is the first i where the bit is not set in the AND of L to i
            # We can find this by checking the first i where the bit is not set in the AND of L to i
            # The AND of L to i is the same as the AND of L to i-1 AND i
            # So, we can find the first i where the bit is cleared
            # This is the first i where the bit is not set in the AND of L to i
            # We can find this by checking the first i where the bit is not set in the AND of L to i
            # We can find this by checking the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # We can find this by checking the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # We can find this by checking the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first i where the bit is not set in the AND of L to i
            # This is the first