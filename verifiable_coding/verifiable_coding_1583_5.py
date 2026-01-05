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
        man_dist = abs(sx - ex) + abs(sy - ey)
        
        # Check if the bomb is on the direct path
        # If the bomb is on the direct path, then we need to detour
        # Check if the bomb is between start and end
        if (bx == sx and by == sy) or (bx == ex and by == ey):
            # Bomb is at start or end, but problem states all three are distinct
            # So this case is not possible
            pass
        
        # Check if bomb is on the straight line path
        # If the bomb is on the straight line path, then we need to detour
        # Check if the bomb is between start and end
        if (sx <= bx <= ex or ex <= bx <= sx) and (sy <= by <= ey or ey <= by <= sy):
            # Bomb is on the straight line path, so need to detour
            # The detour adds 2 steps (go around the bomb)
            man_dist += 2
        
        results.append(str(man_dist))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()