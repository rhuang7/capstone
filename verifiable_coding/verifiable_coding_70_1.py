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
        
        # The k-complete word must be a palindrome and have period k
        # So each position i in the first k positions determines the entire word
        # Because of the period k, the word is made of repeated blocks of size k
        # And because it's a palindrome, the first half of the block determines the second half
        
        # For each block of size k, we need to make it a palindrome
        # So for each position in the first half of the block, we need to make sure it matches the corresponding position in the second half
        
        # The number of blocks is n // k
        # Each block has size k
        # For each block, we need to check the first half of the block and make sure it matches the second half
        
        # For each block, we need to find the minimum number of changes to make it a palindrome
        # We can do this by checking each pair of positions (i, k - i - 1) in the block
        # And count the number of mismatches
        
        total_changes = 0
        
        for block_num in range(n // k):
            block_start = block_num * k
            block_end = block_start + k
            # For each position in the first half of the block
            for i in range(k // 2):
                pos1 = block_start + i
                pos2 = block_start + k - i - 1
                if s[pos1] != s[pos2]:
                    total_changes += 1
        
        results.append(str(total_changes))
    
    print('\n'.join(results))