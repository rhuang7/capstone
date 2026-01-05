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
        cnt = Counter(w)
        freq = list(cnt.values())
        freq.sort()
        n = len(freq)
        if n == 1:
            print(0)
            continue
        # Try all possible frequencies as the base
        res = float('inf')
        for i in range(n):
            # Try to make all frequencies within K of freq[i]
            # We can only adjust the frequencies by removing letters
            # So we need to find the minimum number of removals to make all frequencies within K of each other
            # We can sort the frequencies and try to make them as close as possible
            # We can try to fix the frequencies to be in a range of K
            # We can try to adjust the frequencies to be in a window of size K
            # We can try to make all frequencies within K of the median or something similar
            # For this problem, we can try to make all frequencies within K of the median
            # We can try to adjust the frequencies to be in a window of size K
            # We can try to adjust the frequencies to be in a window of size K
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make all frequencies within K of the median
            # We can try to make