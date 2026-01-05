import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    health = list(map(int, data[1:n+1]))
    P = int(data[n+1])
    
    # Sort the crystals by health in ascending order
    health.sort()
    
    points = 0
    for h in health:
        if P >= h:
            # Use the first action: destroy the crystal and gain 1 point
            P -= h
            points += 1
        else:
            # Use the second action: refuel the laser using 1 point
            # This is only possible if we have at least 1 point
            if points > 0:
                P += h
                points -= 1
            else:
                # No points to refuel, cannot perform this action
                pass
    print(points)

if __name__ == '__main__':
    solve()