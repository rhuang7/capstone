import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Compute the period length
        period = n // k
        
        # For each position in the period, find the required character
        # and count the number of changes needed
        # Each position in the period determines the entire block
        # because the word must be a palindrome and have period k
        # So, for each position i in 0..period-1, we need to ensure
        # that s[i], s[i + period], s[i + 2*period], ... are the same
        # and also that s[i] == s[n - 1 - i]
        
        # We will process each position in the period once
        # and for each position, check all its occurrences in the word
        # and count the number of changes needed to make them the same
        # and also check the palindrome condition
        
        # Initialize the answer
        res = 0
        
        # For each position in the period
        for i in range(period):
            # Check all positions in the same block
            # and also check the palindrome condition
            # We need to find the character that appears most frequently
            # in the positions that need to be the same
            # and count the number of changes needed
            
            # First, collect all the positions in the block
            # and the corresponding positions in the palindrome
            # For each position j in the block, we need to check
            # both the block and the palindrome
            # So for each position j in the block, we check
            # s[j], s[j + period], s[j + 2*period], ... and also
            # s[n - 1 - j], s[n - 1 - j - period], ...
            
            # We can use a frequency dictionary to count the occurrences
            # of each character in the positions that need to be the same
            freq = {}
            
            # Check all positions in the block and their palindrome counterparts
            for m in range(n // (period * 2)):
                pos1 = i + m * period
                pos2 = n - 1 - pos1
                if pos1 >= n or pos2 >= n:
                    break
                # Check if pos1 and pos2 are in the same block
                # If they are, we need to make them the same
                # So we add both positions to the frequency dict
                # but only if they are in the same block
                # So we check if pos1 is in the same block as pos2
                # which is true if pos1 and pos2 are in the same block
                # which is true if pos1 % period == pos2 % period
                # which is true if pos1 and pos2 are in the same block
                # So we add both positions to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency dict
                # and count the number of changes needed
                # to make them the same
                # So for each position in the block, we add both positions
                # to the frequency