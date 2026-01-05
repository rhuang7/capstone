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
        
        # Compute the number of blocks
        block_size = n // k
        total = 0
        
        # For each block, check the required character
        for i in range(block_size):
            # The first occurrence of the block is at position i * k
            first_pos = i * k
            # The last occurrence of the block is at position (i + 1) * k - 1
            last_pos = (i + 1) * k - 1
            # The required character is s[first_pos]
            required_char = s[first_pos]
            
            # Check all positions in the block
            for j in range(first_pos, last_pos + 1):
                if s[j] != required_char:
                    total += 1
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()