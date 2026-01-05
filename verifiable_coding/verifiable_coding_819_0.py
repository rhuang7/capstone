import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        # Initial state: 1 red, 1 black
        r = 1
        b = 1
        
        # Perform operations until either r or b becomes 0
        while r > 0 and b > 0:
            if r >= b:
                r -= b
            else:
                b -= r
        
        # Check if we can reach the required number of balls
        if r == x and b == y:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()