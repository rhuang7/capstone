import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        sx = int(data[idx+1])
        sy = int(data[idx+2])
        ex = int(data[idx+3])
        ey = int(data[idx+4])
        bx = int(data[idx+5])
        by = int(data[idx+6])
        idx += 7
        
        # Calculate Manhattan distance between start and end
        moves = abs(sx - ex) + abs(sy - ey)
        
        # Check if the bomb is on the direct path
        # If the bomb is on the direct path, we need to go around it
        # Check if the bomb is on the straight line between start and end
        # If the bomb is on the straight line, we need to detour
        # Check if the bomb is between start and end
        if (sx == ex or sy == ey) and (bx == ex or by == ey):
            # Check if the bomb is on the straight line
            if (sx == bx and sy == by) or (sx == bx and sy == ey) or (sx == ex and sy == by) or (sx == ex and sy == ey):
                # Bomb is on the direct path, need to detour
                # The minimum detour is 2 steps (go around the bomb)
                moves += 2
        
        results.append(str(moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()