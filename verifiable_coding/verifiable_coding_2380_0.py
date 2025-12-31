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
        
        # If k is 1, the garland must have all lamps on or all off
        if k == 1:
            # Count the number of 1s and 0s
            ones = s.count('1')
            zeros = n - ones
            # The minimum moves is the minimum of converting all to 1 or all to 0
            results.append(min(ones, zeros))
            continue
        
        # For k > 1, the garland must have lamps on at positions i, i + k, i + 2k, ...
        # So we need to find all positions where lamps should be on, and count the changes needed
        
        # The positions where lamps should be on are those congruent to pos mod k, where pos is the first on lamp
        # So we need to try all possible starting positions (0 to k-1)
        min_moves = float('inf')
        
        # Try all possible starting positions for the first on lamp
        for start in range(k):
            # Positions where lamps should be on
            positions = [start + i * k for i in range(n // k + 1)]
            
            # Count the number of changes needed
            changes = 0
            for pos in positions:
                if s[pos] != '1':
                    changes += 1
            
            # Update the minimum moves
            min_moves = min(min_moves, changes)
        
        results.append(min_moves)
    
    # Output all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()