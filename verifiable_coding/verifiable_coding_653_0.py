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
    for h in health:
        # Try to destroy the crystal using the first action
        if P >= h:
            points += 1
            P -= h
        else:
            # Try to destroy the crystal using the second action
            if points > 0:
                points -= 1
                P += h
            else:
                # Cannot destroy this crystal with either action
                continue
    
    print(points)

if __name__ == '__main__':
    solve()