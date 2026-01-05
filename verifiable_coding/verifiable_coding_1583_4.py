import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        sx = int(input[idx+1])
        sy = int(input[idx+2])
        ex = int(input[idx+3])
        ey = int(input[idx+4])
        bx = int(input[idx+5])
        by = int(input[idx+6])
        idx += 7
        
        # Calculate Manhattan distance between start and end
        dist = abs(sx - ex) + abs(sy - ey)
        
        # Check if the bomb is on the direct path
        # If the bomb is on the direct path, we need to detour
        # Check if the bomb is between start and end
        if (sx <= bx <= ex or ex <= bx <= sx) and (sy <= by <= ey or ey <= by <= sy):
            # Detour: go around the bomb
            # The minimum detour is 2 (go around the bomb)
            dist += 2
        
        print(dist)

if __name__ == '__main__':
    solve()