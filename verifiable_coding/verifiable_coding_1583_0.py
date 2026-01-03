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
        # If the bomb is on the direct path, we need to detour
        # Check if the bomb is between start and end
        # If the bomb is on the direct path, the minimum moves is moves + 2
        # Because Jerry has to go around the bomb (either up or down)
        # But if the bomb is not on the direct path, the moves remain the same
        
        # Check if the bomb is on the direct path
        # The direct path is from (sx, sy) to (ex, ey)
        # If the bomb is on the same row or column and between the start and end
        if (bx == sx and bx == ex and (sy <= by <= ey or ey <= by <= sy)) or \
           (by == sy and by == ey and (sx <= bx <= ex or ex <= bx <= sx)) or \
           (bx == ex and by == ey and (sx <= bx <= ex or ex <= bx <= sx)) or \
           (bx == sx and by == sy and (ex <= bx <= sx or sx <= bx <= ex)):
            # Bomb is on the direct path, need to detour
            # The minimum detour is 2 moves (go around the bomb)
            moves += 2
        
        results.append(str(moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()