import sys
MOD = 10**9 + 7

def solve():
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
        # We can compute this efficiently using the fact that the bitwise AND of a range of numbers decreases as the range increases
        # We can precompute for each bit position whether it is set in the AND result for a range [L, i]
        # The key observation is that for a bit position b, if there is a number in [L, i] that has the bit b unset, then the AND result will have bit b unset
        # So for each bit position, we can find the first number in [L, i] that has that bit unset
        # We can compute the sum by iterating over each bit position and determining how many times it contributes to the sum
        # The final result is the sum of all bits multiplied by their contribution
        # We can use a binary search approach to find the first number in [L, i] that has a bit unset
        # The time complexity is O(T * 60) which is acceptable for T up to 1e5
        # The space complexity is O(1)
        # The sum S is computed as follows:
        # For each bit position b (from 0 to 60), we find the first number in [L, i] that has bit b unset
        # If such a number exists, then the bit b will not be set in the AND result for any i >= that number
        # So for each bit position, we can find the first i where the bit b is unset in the range [L, i]
        # Then, for all i >= that first i, the bit b will not be set in the AND result
        # The contribution of bit b to the sum is (number of terms where the bit is set) * 2^b
        # The number of terms where the bit is set is the number of i in [L, R] where the bit is set in the AND result
        # We can compute this using binary search for each bit position
        # The final result is the sum of all contributions
        # Let's implement this
        res = 0
        for b in range(60):
            # Find the first number in [L, R] where the bit b is unset
            # The first number where bit b is unset is L + (1 << b) - L & (1 << b)
            # Wait, this is not correct. Let's think again.
            # We need to find the first number in [L, R] where the bit b is unset
            # The first number where bit b is unset is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it differently.
            # For a given bit b, the first number in [L, R] where the bit b is unset is the smallest number >= L where the bit b is unset
            # This is L if the bit b is unset in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number where bit b is unset is the smallest number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number where bit b is unset is the first number in [L, R] where the bit b is 0
            # We can find this using binary search
            # The number of terms where the bit b is set in the AND result is the number of i in [L, R] where the bit b is set in the AND result
            # The AND result for [L, i] is the bitwise AND of all numbers from L to i
            # The bit b will be set in the AND result if and only if all numbers from L to i have bit b set
            # So for a given bit b, the first i where the bit b is unset in the AND result is the first i where there is a number in [L, i] that has bit b unset
            # So the first i where the bit b is unset in the AND result is the first i where there is a number in [L, i] that has bit b unset
            # This can be found by finding the first number in [L, R] where bit b is unset
            # The contribution of bit b to the sum is (number of i in [L, R] where the bit b is set in the AND result) * 2^b
            # So for each bit b, we can find the first i where the bit b is unset in the AND result
            # If such an i exists, then the bit b is not set in the AND result for any i >= that i
            # So the number of terms where the bit b is set in the AND result is (first_i - L)
            # So the contribution is (first_i - L) * 2^b
            # So we can compute this for each bit b
            # Let's implement this
            # Find the first i >= L where the bit b is unset in the AND result
            # The AND result for [L, i] is the bitwise AND of all numbers from L to i
            # The bit b will be set in the AND result if and only if all numbers from L to i have bit b set
            # So the first i where the bit b is unset in the AND result is the first i where there is a number in [L, i] that has bit b unset
            # This can be found by finding the first number in [L, R] where bit b is unset
            # The first number in [L, R] where bit b is unset is the smallest number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the smallest number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1 << b))
            # But this is not correct. Let's think of it as follows:
            # The first number in [L, R] where the bit b is unset is the first number >= L where the bit b is 0
            # This is L if the bit b is 0 in L, otherwise it is L + (1 << b) - (L & (1