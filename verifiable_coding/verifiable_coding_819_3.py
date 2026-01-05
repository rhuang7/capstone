import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        
        # Initial state: 1 red, 1 black
        R = 1
        B = 1
        
        # Perform operations until R or B is 0
        while R > 0 and B > 0:
            if R >= B:
                R -= B
            else:
                B -= R
        
        # Check if we can reach the desired counts
        if R == x and B == y:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()