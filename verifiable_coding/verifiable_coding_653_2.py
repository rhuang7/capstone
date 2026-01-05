import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    health = list(map(int, data[1:n+1]))
    P = int(data[n+1])
    
    # Sort the crystals by health
    health.sort()
    
    points = 0
    # Try to take each crystal in order
    for h in health:
        if P >= h:
            # Use the first action: destroy the crystal and gain 1 point
            P -= h
            points += 1
        else:
            # Try to use the second action: refuel using points
            # We need at least 1 point to do this
            if points > 0:
                # Refuel the laser using 1 point
                P += h
                points -= 1
            # If we can't refuel, we can't take this crystal
            # So we break the loop as we can't take any more crystals
            break
    
    print(points)

if __name__ == '__main__':
    solve()