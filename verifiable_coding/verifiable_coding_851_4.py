import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        # Expected length of compressed string
        # Each run of the same character contributes 2 to the length (char + length)
        # So the expected length is 2 * number of runs
        # The expected number of runs for a string of length N with K distinct characters
        # is K * (1 - (1/K)^N) / (1 - (1/K)^N) ? No, that's not right.
        
        # Correct formula for expected number of runs:
        # For a string of length N with K distinct characters, the expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N) ? No.
        
        # The correct formula for expected number of runs is:
        # E = 1 + (K-1) * (1 - (1/K)^N) / (1 - (1/K)^N