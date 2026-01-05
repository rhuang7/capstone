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
        
        count = collections.Counter(w)
        freq = list(count.values())
        freq.sort()
        
        # Try to find the minimum number of removals
        # by trying all possible frequencies that can be adjusted to make it K-good
        min_removals = float('inf')
        
        # Try all possible base frequencies
        for i in range(len(freq)):
            # Try to make all frequencies as close as possible to freq[i]
            # by adjusting others
            # We can try to make all frequencies in [freq[i] - K, freq[i] + K]
            # but it's easier to try to make all frequencies as close as possible to the median
            # or to try to adjust the frequencies to be within K of each other
            # So we try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to the median
            # or to the middle of the sorted list
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies within K of each other
            # by adjusting the frequencies
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make the frequencies as close as possible to each other
            # by reducing some of them
            
            # Try to make all frequencies as close as possible to each other
            # by reducing some of them
            # We can try to make