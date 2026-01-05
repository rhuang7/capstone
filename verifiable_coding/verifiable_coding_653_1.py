import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    health = list(map(int, data[1:n+1]))
    P = int(data[n+1])
    
    # Sort crystals by health in ascending order
    health.sort()
    
    points = 0
    # Try to take each crystal in order
    for h in health:
        # If we can take this crystal with the current energy
        if P >= h:
            points += 1
            P -= h
        else:
            # Try to use a point to refuel
            if points > 0:
                points -= 1
                P += h
            else:
                # Can't do anything, break
                break
    print(points)

if __name__ == '__main__':
    solve()