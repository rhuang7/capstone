import sys
import math

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
        # We can observe that the bitwise AND of a range of numbers
        # will eventually become 0 once a number with a 0 in a bit position
        # is included. So we can find the first i where the AND becomes 0
        # and compute the sum accordingly
        # Let's find the first i where the AND of L to i becomes 0
        # This is equivalent to finding the first i where i has a 0 in the
        # same bit position as L
        # We can compute this by finding the next number with a 0 in the
        # same bit position as L
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # We can find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L to i becomes 0
        # This is the first i where i has a 0 in the same bit position as L
        # Let's find the next number with a 0 in the same bit position as L
        # by finding the next number with a 1 in that position
        # Let's find the first i where the AND of L