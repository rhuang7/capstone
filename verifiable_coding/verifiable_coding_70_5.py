import sys
import math

def solve():
    import sys
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
        
        # For a k-complete word, the word must be a palindrome and have period k
        # So, the word is made of m = n/k repeated blocks of size k
        # Each block must be a palindrome and all blocks must be the same
        m = n // k
        
        # For each block, we need to make it a palindrome and all blocks must be the same
        # So, for each position in the block, we need to check if it matches its mirror
        # and also ensure that all blocks are the same
        
        # We will process each block and count the number of changes needed to make it a palindrome
        # Then, we will ensure all blocks are the same
        
        # First, process each block to make it a palindrome
        # We will store the first occurrence of each block and compare others to it
        # To minimize changes, we choose the block with the least changes to be the target
        
        # Collect all blocks
        blocks = []
        for i in range(m):
            start = i * k
            end = start + k
            block = s[start:end]
            blocks.append(block)
        
        # For each block, count the number of changes needed to make it a palindrome
        # Also, track the most frequent character in the block to minimize changes
        min_changes = float('inf')
        best_block = None
        
        for block in blocks:
            # Count the number of changes needed to make this block a palindrome
            changes = 0
            for i in range(k // 2):
                if block[i] != block[k - 1 - i]:
                    changes += 1
            # Track the most frequent character in the block
            freq = {}
            for c in block:
                freq[c] = freq.get(c, 0) + 1
            max_freq = max(freq.values())
            # The minimal changes to make the block a palindrome is changes
            # But we also need to make sure all blocks are the same
            # So we need to choose the block with the least changes to be the target
            # So we track the block with the least changes
            if changes < min_changes:
                min_changes = changes
                best_block = block
        
        # Now, for all other blocks, we need to change them to best_block
        # So for each block, count the number of characters that differ from best_block
        total_changes = min_changes
        for block in blocks:
            if block == best_block:
                continue
            changes = 0
            for i in range(k):
                if block[i] != best_block[i]:
                    changes += 1
            total_changes += changes
        
        results.append(str(total_changes))
    
    print('\n'.join(results))