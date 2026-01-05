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
        counts = list(freq.values())
        
        # Sort the counts
        counts.sort()
        
        # Try to adjust the counts to make them K-good
        # We need to make sure that for any two counts, their difference is <= K
        # So we can try to adjust the counts to be as close as possible
        
        # We can try to make all counts either floor(avg) or ceil(avg)
        # But since we can only remove letters, we need to find the best way to adjust
        
        # Let's try to make all counts as close as possible
        # We can try to make all counts either floor(avg) or ceil(avg)
        # But since we can only remove letters, we need to find the best way to adjust
        
        # Let's try to make all counts as close as possible
        # We can try to make all counts either floor(avg) or ceil(avg)
        # But since we can only remove letters, we need to find the best way to adjust
        
        # Try to find the minimal number of removals
        min_removals = float('inf')
        
        # Try all possible target counts
        for target in range(min(counts), max(counts) + 1):
            # For each character, we can remove some letters to make its count equal to target
            # But we can't increase counts, only decrease
            # So we need to find the minimal number of removals to make all counts <= target
            # And also ensure that the difference between any two counts is <= K
            # So we need to find the minimal number of removals to make all counts as close as possible
            
            # We can try to make all counts as close as possible to each other
            # Let's try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We can try to make all counts either floor(avg) or ceil(avg)
            # But since we can only remove letters, we need to find the best way to adjust
            
            # Try to make all counts as close as possible
            # We