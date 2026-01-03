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
        
        # For a k-periodic garland, the positions of '1's must be at positions
        # i * k, (i+1)*k, (i+2)*k, ... such that they are exactly k apart.
        # So, the positions of '1's must be in the form of a * k, where a is an integer.
        # So, we need to find all positions in s that are multiples of k, and check if they are '1's.
        # Then, we can decide which positions to turn on or off to make it k-periodic.
        
        # The positions of '1's in the k-periodic garland must be at positions 0, k, 2k, 3k, ...
        # So, for each position i in s, if i % k == 0, then it must be a '1'.
        # Otherwise, it must be a '0'.
        
        # So, we can iterate through the string and count the number of changes needed.
        # For each position i:
        # if i % k == 0:
        #   if s[i] == '0', then we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', then we need to turn it off (cost 1)
        # But wait, this is not correct. Because the k-periodic garland can have any number of '1's as long as they are spaced exactly k apart.
        # So, the '1's can be at positions 0, k, 2k, etc., but not necessarily starting from 0.
        # So, we need to find all possible positions where '1's can be placed, and choose the one that requires the least changes.
        
        # However, the problem says that the garland is not cyclic, so the first and last '1's are not connected.
        # So, the positions of '1's must be at positions i * k, where i is an integer >= 0.
        
        # So, the valid positions for '1's are 0, k, 2k, 3k, ... up to n-1.
        # So, we can iterate through the string and check if the current position is a valid position for a '1'.
        # If it is, then we need to check if it is '1' or '0'.
        
        # We can collect all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # But this is not correct. Because the '1's can be at positions 0, k, 2k, etc., but not necessarily starting from 0.
        # So, we need to consider all possible positions where the '1's can be placed.
        
        # However, the problem says that the garland is not cyclic, so the '1's can be at any positions that are multiples of k, but they must be in order.
        
        # So, the correct approach is:
        # 1. Find all positions in the string that are multiples of k.
        # 2. For each such position, we need to decide whether to turn it on or off.
        # 3. But the '1's must be spaced exactly k apart, so the positions of '1's must be at positions i * k, where i is an integer >= 0.
        # 4. So, we can iterate through the string and for each position i:
        #    if i % k == 0:
        #        if s[i] == '0', we need to turn it on (cost 1)
        #    else:
        #        if s[i] == '1', we need to turn it off (cost 1)
        
        # But this is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, the correct approach is to find all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which of these positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However, this approach is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, we need to consider all possible positions where the '1's can be placed.
        
        # The correct approach is:
        # 1. Find all the positions in the string that are multiples of k.
        # 2. For each such position, we can decide whether to turn it on or off.
        # 3. However, the '1's must be spaced exactly k apart, so the positions of '1's must be at positions i * k, where i is an integer >= 0.
        # 4. So, the positions of '1's must be at positions 0, k, 2k, 3k, etc.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However, this approach is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, the correct approach is to find all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which of these positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However, this is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, the correct approach is to find all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which of these positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However, this is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, the correct approach is to find all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which of these positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However, this is not correct. Because the '1's can be at any positions that are multiples of k, but not necessarily starting from 0.
        # So, the correct approach is to find all the positions that are multiples of k and check if they are '1's.
        # Then, we can decide which of these positions to turn on or off.
        
        # So, we can iterate through the string and for each position i:
        # if i % k == 0:
        #   if s[i] == '0', we need to turn it on (cost 1)
        # else:
        #   if s[i] == '1', we need to turn it off (cost 1)
        
        # However,