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
        
        # Edge case: if t3 is exactly t1 or t2
        if t3 == t1:
            # Check if we can get at least v3 volume by taking only from first bucket
            if v1 >= v3:
                print("YES")
            else:
                print("NO")
            continue
        if t3 == t2:
            # Check if we can get at least v3 volume by taking only from second bucket
            if v2 >= v3:
                print("YES")
            else:
                print("NO")
            continue
        
        # Check if the temperature is achievable
        if (v1 * (t1 - t3) == v2 * (t3 - t2)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()