import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    idx = 1
    
    for _ in range(n):
        v1 = int(data[idx])
        t1 = int(data[idx+1])
        v2 = int(data[idx+2])
        t2 = int(data[idx+3])
        v3 = int(data[idx+4])
        t3 = int(data[idx+5])
        idx += 6
        
        # Check if it's possible to get exactly t3 temperature with at least v3 volume
        # The temperature of the mixture is (v1*t1 + v2*t2) / (v1 + v2)
        # We need (v1*t1 + v2*t2) / (v1 + v2) = t3
        # => v1*t1 + v2*t2 = t3*(v1 + v2)
        # => v1*(t1 - t3) = v2*(t3 - t2)
        # If t1 == t3 and t2 == t3, then it's possible
        # If t1 == t3 and t2 != t3, then we need v1 + v2 >= v3
        # If t2 == t3 and t1 != t3, then we need v1 + v2 >= v3
        # If t1 < t3 < t2, then it's impossible
        # If t3 is between t1 and t2, then we need to find v1 and v2 such that the mixture is exactly t3
        # Check if t3 is between t1 and t2
        if t1 > t3 or t2 < t3:
            print("NO")
            continue
        
        # Check if t3 is equal to t1 or t2
        if t1 == t3 and t2 == t3:
            # All water is at the same temperature
            if v1 + v2 >= v3:
                print("YES")
            else:
                print("NO")
            continue
        elif t1 == t3:
            # Only use the first bucket
            if v1 >= v3:
                print("YES")
            else:
                print("NO")
            continue
        elif t2 == t3:
            # Only use the second bucket
            if v2 >= v3:
                print("YES")
            else:
                print("NO")
            continue
        
        # Check if it's possible to mix v1 and v2 to get exactly t3
        # The required ratio is v1 / v2 = (t3 - t2) / (t1 - t3)
        # So v1 * (t1 - t3) = v2 * (t3 - t2)
        if v1 * (t1 - t3) == v2 * (t3 - t2):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()