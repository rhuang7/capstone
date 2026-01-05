import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    idx = 1
    results = []
    
    for _ in range(n):
        v1 = int(data[idx])
        t1 = int(data[idx+1])
        v2 = int(data[idx+2])
        t2 = int(data[idx+3])
        v3 = int(data[idx+4])
        t3 = int(data[idx+5])
        idx += 6
        
        # Check if it's possible to get exactly t3 temperature with at least v3 volume
        # Let x be the volume of cold water used, y be the volume of hot water used
        # x + y >= v3
        # (x*t1 + y*t2) / (x + y) == t3
        
        # Rearranging the temperature equation:
        # x*t1 + y*t2 = t3*(x + y)
        # x*(t1 - t3) + y*(t2 - t3) = 0
        
        # We need to find x and y such that:
        # x + y >= v3
        # x >= 0, y >= 0
        # x <= v1, y <= v2
        
        # Let's check if it's possible to get exactly t3 temperature with exactly v3 volume
        # If possible, then it's also possible to get more than v3 volume (by adding more water)
        
        # Check if t3 is between t1 and t2
        if t3 < t1 or t3 > t2:
            results.append("NO")
            continue
        
        # Check if t3 is exactly t1 or t2
        if t3 == t1:
            if v1 >= v3:
                results.append("YES")
            else:
                results.append("NO")
            continue
        if t3 == t2:
            if v2 >= v3:
                results.append("YES")
            else:
                results.append("NO")
            continue
        
        # Now, t3 is between t1 and t2
        # We need to find x and y such that:
        # x*(t1 - t3) + y*(t2 - t3) = 0
        # x + y = v3
        
        # Solve for x and y
        # x = (y * (t2 - t3)) / (t1 - t3)
        # x + y = v3
        
        # Let's try to find integer solutions
        # We can iterate over possible y values from 0 to v2
        # and check if x is within [0, v1]
        
        found = False
        for y in range(0, v2 + 1):
            if y > v3:
                continue
            x = (y * (t2 - t3)) / (t1 - t3)
            if x.is_integer() and 0 <= x <= v1 and x + y == v3:
                found = True
                break
        
        if found:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()