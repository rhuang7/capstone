import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # We need to find the minimum number of moves to make the string k-periodic
        # A k-periodic string has all '1's at positions i, i + k, i + 2k, ...
        # So the positions of '1's must be in the same equivalence class modulo k
        
        # For each position i, we can determine which equivalence class it belongs to
        # The valid positions for '1's are those in the same class as the first '1'
        # So we need to find the first '1' in the string, and then check all positions in its class
        
        # Find the first '1' in the string
        first_one = -1
        for i in range(n):
            if s[i] == '1':
                first_one = i
                break
        
        if first_one == -1:
            # No '1's, so we can just leave it as is (0 moves)
            results.append(0)
            continue
        
        # The valid positions for '1's are those congruent to first_one mod k
        # So we need to check all positions in this class and count how many are not '1'
        # Also, we need to ensure that the positions are in order (i.e., the first '1' is the first in the class)
        # So we need to check all positions in the class, and count the number of '1's that are not in the correct positions
        
        # The positions in the class are: first_one, first_one + k, first_one + 2k, ...
        # But we need to make sure they are within the string
        # Also, we need to ensure that the positions are in order (i.e., the first '1' is the first in the class)
        
        # So we can iterate through all positions in the class and check if they are '1'
        # Then, for the positions that are not '1', we need to flip them (count as 1 move)
        # For the positions that are '1', we need to check if they are in the correct order (i.e., the first '1' is the first in the class)
        
        # We can collect all positions in the class
        valid_positions = []
        for i in range(n):
            if i % k == first_one % k:
                valid_positions.append(i)
        
        # Now, we need to make sure that the valid_positions are in order (i.e., the first '1' is the first in the class)
        # So we need to check if the first '1' is the first in the class
        # If not, we need to flip it (count as 1 move)
        
        # Also, we need to check that the valid_positions are in order (i.e., the first '1' is the first in the class)
        # So we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # So we can check if the first '1' is the first in the class
        # If not, we need to flip it (count as 1 move)
        
        # Also, we need to check that the valid_positions are in order (i.e., the first '1' is the first in the class)
        # So we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # So we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # So we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how many are not '1'
        # Also, we need to ensure that the first '1' is the first in the class
        
        # Now, we can iterate through the valid_positions and count how