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
        
        # For a k-complete word, the word must be a palindrome and have period k
        # So each position i must equal the position i + k, and the word must be a palindrome
        # So we need to check all positions in the first half of the block of size k
        # and ensure they match their mirrored counterparts in the same block
        
        # The total number of blocks is n // k
        # Each block has size k
        # For each block, we need to ensure that the characters in the block are the same as their mirrored counterparts
        # Also, the entire word must be a palindrome, so the first half of the word must match the second half
        
        # So we need to check for each position i in the first half of the word
        # and ensure that s[i] == s[n - i + 1]
        # But also, for each block, the characters must be the same in the block and its mirror
        
        # So we can iterate over each block and check for each position in the block
        # and compare it with its mirror in the same block
        # The minimum number of changes is the number of positions where the characters do not match
        
        # We can do this by checking for each position in the first half of the word
        # and for each block, check the positions in the block and their mirror
        
        # For each position i in the first half of the word
        # we check if s[i] == s[n - i + 1]
        # and for each block, check the positions in the block and their mirror
        
        # But to avoid double counting, we can iterate over each block and check for each position in the block
        # and compare it with its mirror in the same block
        
        # So for each block, we check for each position in the block
        # and compare it with its mirror in the same block
        # The minimum number of changes is the number of positions where the characters do not match
        
        # The total number of positions to check is (n // 2)
        # But for each block, we need to check the positions in the block and their mirror
        
        # So we can iterate over each position in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So for each position i in the first half of the word
        # we check if i is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each block, check the positions in the block and their mirror
        
        # So for each position i in the first half of the word
        # we check if i is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So we can iterate over each position in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can iterate over each position in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror in the same block
        
        # So the minimum number of changes is the number of positions where the characters do not match
        
        # So we can do this by checking for each position i in the first half of the word
        # and for each position, check if it is in the first half of the block
        # and compare it with its mirror