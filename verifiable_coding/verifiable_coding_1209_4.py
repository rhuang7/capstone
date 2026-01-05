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
        
        # Let's find if there exists x and y such that:
        # x >= 0, y >= 0, x + y >= v3
        # and x*(t1 - t3) + y*(t2 - t3) = 0
        
        # If t3 is between t1 and t2, then it's possible to mix
        if t1 <= t3 <= t2:
            # Check if it's possible to get exactly t3 with at least v3 volume
            # We can use binary search or check edge cases
            # If t3 == t1, then use all cold water
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
            
            # Check if it's possible to mix some cold and some hot water
            # The required ratio is (t3 - t1) / (t2 - t3)
            # So, we can check if there exists x and y such that:
            # x / y = (t2 - t3) / (t3 - t1)
            # and x + y >= v3
            
            # Let's try to find x and y such that x + y >= v3
            # Let's assume x = (t2 - t3) * k, y = (t3 - t1) * k
            # Then x + y = k * (t2 - t3 + t3 - t1) = k * (t2 - t1)
            # We need k * (t2 - t1) >= v3
            # So k >= v3 / (t2 - t1)
            
            # Let's try k = v3 / (t2 - t1)
            k = v3 / (t2 - t1)
            x = (t2 - t3) * k
            y = (t3 - t1) * k
            
            if x <= v1 and y <= v2 and x + y >= v3:
                results.append("YES")
            else:
                results.append("NO")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()