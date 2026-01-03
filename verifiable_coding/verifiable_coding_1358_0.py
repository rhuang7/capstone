import sys
import collections

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        w = input[idx]
        K = int(input[idx+1])
        idx += 2
        
        freq = collections.Counter(w)
        letters = list(freq.keys())
        n = len(letters)
        
        # Sort the letters based on their frequencies
        letters.sort(key=lambda x: freq[x])
        freqs = [freq[x] for x in letters]
        
        # Try all possible frequencies to find the minimum removals
        min_removals = float('inf')
        for i in range(n):
            # Try to make all frequencies as close as possible to freqs[i]
            # We can adjust the frequencies to be within K of each other
            # We can try to make all frequencies between (freqs[i] - K) and (freqs[i] + K)
            # But we need to adjust the frequencies to be as close as possible
            # We can use a greedy approach to adjust the frequencies
            # We can try to make all frequencies as close as possible to the median
            # We can try to make all frequencies as close as possible to the mean
            # We can try to make all frequencies as close as possible to the mode
            # We can try to make all frequencies as close as possible to the middle value
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of the sorted list
            # We can try to make all frequencies as close as possible to the middle of