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
        # The temperature of the mixture is (v1*t1 + v2*t2) / (v1 + v2)
        # We need (v1*t1 + v2*t2) / (v1 + v2) = t3
        # => v1*t1 + v2*t2 = t3*(v1 + v2)
        # => v1*(t1 - t3) = v2*(t3 - t2)
        
        # Check if the desired temperature is achievable
        # Also, check if the total volume is at least v3
        # We can take any amount from the two buckets as long as the total is >= v3
        
        # Case 1: Take all from bucket 1
        if v1 >= v3 and t1 == t3:
            print("YES")
            continue
        # Case 2: Take all from bucket 2
        if v2 >= v3 and t2 == t3:
            print("YES")
            continue
        
        # Check if the desired temperature is achievable
        if (v1 * (t1 - t3) == v2 * (t3 - t2)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()