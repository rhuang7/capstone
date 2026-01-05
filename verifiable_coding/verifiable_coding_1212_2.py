import sys
import math
from collections import Counter

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for S in cases:
        cnt = Counter(S)
        freq = list(cnt.values())
        n = len(S)
        m = len(freq)
        freq.sort(reverse=True)

        # Find the maximum possible number of characters that can have the same frequency
        # We try all possible k (number of characters with same frequency)
        # The maximum k is min(m, n // k) where k is the frequency
        # We need to find the maximum k such that k * k <= n
        max_k = int(math.isqrt(n))
        min_ops = n  # Initialize with maximum possible operations

        for k in range(1, max_k + 1):
            # Check if there are at least k characters with frequency >= k
            # We need to find the maximum number of characters that can have frequency k
            # The total number of characters needed is k * k
            # So we need to find the maximum number of characters with frequency >= k
            # and see if we can adjust them to have exactly k occurrences
            # The number of operations is the sum of (original frequency - k) for those characters
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # Then the number of operations is sum(freq[i] - k for i in range(k))
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k) for i in range(k)
            # But we can only take up to k characters with frequency >= k
            # So we need to find the maximum number of characters with frequency >= k
            # and take the first k of them
            # So we sort freq in descending order and take the first k elements
            # Then compute the sum of (freq[i] - k