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
        # A k-periodic string has on-lamps at positions i, i + k, i + 2k, ... etc.
        # So the positions of on-lamps must be in the form of i + m*k for some m >= 0
        
        # We can try all possible starting positions for the first on-lamp
        # The first on-lamp can be at any position in the first k positions (0-based)
        # Because after that, the on-lamps must be at positions i, i + k, i + 2k, etc.
        
        min_moves = float('inf')
        
        # Try all possible starting positions for the first on-lamp
        for start in range(k):
            # The positions of on-lamps are start, start + k, start + 2k, ...
            # We need to check which positions are on and which are off
            # And calculate the number of moves required to make them k-periodic
            
            # Initialize the number of moves
            moves = 0
            
            # Iterate through all positions in the string
            for i in range(n):
                # Check if this position is in the k-periodic sequence
                if (i - start) % k == 0:
                    # This is a position that should be on
                    if s[i] == '0':
                        moves += 1
                else:
                    # This is a position that should be off
                    if s[i] == '1':
                        moves += 1
            
            # Update the minimum moves
            min_moves = min(min_moves, moves)
        
        results.append(str(min_moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()