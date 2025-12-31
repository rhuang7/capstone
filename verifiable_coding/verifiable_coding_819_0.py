import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        # Initial state: 1 red, 1 black
        R = 1
        B = 1
        
        # Perform operations until R or B becomes 0
        while R > 0 and B > 0:
            # Choose to buy B red balls
            R += B
            # Or choose to buy R black balls
            B += R
            
            # Check if we have enough balls
            if R >= x and B >= y:
                print("YES")
                break
            # If one of them is 0, we can't proceed
            if R == 0 or B == 0:
                print("NO")
                break
        
        # If loop ends without breaking, check if we have enough balls
        if R >= x and B >= y:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()