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
        
        # Check if k is 1
        if k == 1:
            # All lamps must be turned on or off in a way that every adjacent pair is exactly 1 apart
            # So the entire string must be all 0s or all 1s
            # Count the number of 0s and 1s
            cnt0 = s.count('0')
            cnt1 = n - cnt0
            results.append(min(cnt0, cnt1))
            continue
        
        # For k > 1, the garland must have lamps turned on at positions i, i + k, i + 2k, ...
        # So the positions of the lamps must be in the form of i mod k == pos for some pos
        # We need to find all possible positions where lamps can be turned on
        # For each possible starting position (0 to k-1), we can try to create a k-periodic garland
        # and compute the minimal moves required
        
        min_moves = float('inf')
        
        # Try each possible starting position in 0..k-1
        for pos in range(k):
            # The positions where lamps can be turned on are pos, pos + k, pos + 2k, ...
            # We need to count how many lamps are already on at these positions
            # and how many need to be turned on
            on_count = 0
            for i in range(pos, n, k):
                if s[i] == '1':
                    on_count += 1
            # The number of lamps that need to be turned on is (on_count)
            # The number of lamps that need to be turned off is (number of positions in the pattern that are not on)
            # The total number of lamps in the pattern is (n + k - 1) // k
            total_in_pattern = (n + k - 1) // k
            # The number of lamps that need to be turned off is (total_in_pattern - on_count)
            # The total moves is (total_in_pattern - on_count) + (number of lamps not in the pattern that are on)
            # The number of lamps not in the pattern is (n - total_in_pattern)
            # The number of lamps not in the pattern that are on is (s.count('1') - on_count)
            # So total moves is (total_in_pattern - on_count) + (s.count('1') - on_count)
            moves = (total_in_pattern - on_count) + (s.count('1') - on_count)
            if moves < min_moves:
                min_moves = moves
        
        results.append(min_moves)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()