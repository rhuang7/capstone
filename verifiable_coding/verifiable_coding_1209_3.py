import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    index = 1
    
    for _ in range(n):
        v1 = int(data[index])
        t1 = int(data[index+1])
        v2 = int(data[index+2])
        t2 = int(data[index+3])
        v3 = int(data[index+4])
        t3 = int(data[index+5])
        index += 6
        
        # Check if it's possible to get exactly t3 temperature with at least v3 volume
        # The required temperature t3 must be between t1 and t2
        if t3 < t1 or t3 > t2:
            print("NO")
            continue
        
        # Check if we can mix some amount from both buckets to get t3
        # Let x be the amount of cold water, y be the amount of hot water
        # x + y >= v3
        # (x*t1 + y*t2) / (x + y) = t3
        # => x*t1 + y*t2 = t3*(x + y)
        # => x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y*(t3 - t2)/(t1 - t3)
        # Since t1 < t3 < t2, t3 - t2 is negative and t1 - t3 is negative, so x is positive
        
        # Find the minimum amount of cold and hot water needed to get t3
        # Let's try to find if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        
        # Try to find x and y such that x + y = v3
        # (x*t1 + y*t2) / v3 = t3
        # x*t1 + y*t2 = t3 * v3
        # y = v3 - x
        # x*t1 + (v3 - x)*t2 = t3 * v3
        # x*(t1 - t2) + v3*t2 = t3 * v3
        # x = (t3 * v3 - v3 * t2) / (t1 - t2)
        # x = v3 * (t3 - t2) / (t1 - t2)
        
        # Check if x is non-negative and y = v3 - x is non-negative
        # Also, check if x is within the available cold water and y is within the available hot water
        
        # Calculate x
        numerator = v3 * (t3 - t2)
        denominator = t1 - t2
        x = numerator / denominator
        
        if x <= v1 and (v3 - x) <= v2 and x >= 0 and (v3 - x) >= 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()