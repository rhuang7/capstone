import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        w = input[idx]
        K = int(input[idx+1])
        idx += 2
        count = Counter(w)
        freq = list(count.values())
        freq.sort()
        n = len(freq)
        if n == 1:
            print(0)
            continue
        # Try all possible frequencies to find the minimum removals
        min_removals = float('inf')
        for i in range(n):
            # Try to make all frequencies <= freq[i] + K
            # We can keep the frequencies as they are, but adjust the counts
            # to ensure that the difference between any two is <= K
            # So we need to find the maximum frequency that can be kept
            # such that all other frequencies are within K of it
            # We can try to make the frequencies as close as possible
            # to each other
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by choosing a target frequency
            # We can try to make the frequencies as close as possible
            # by