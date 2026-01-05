import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Check if the command string can be executed starting from any cell without going out of bounds
        safe = False
        
        # Try all possible starting positions
        for i in range(n):
            for j in range(m):
                x, y = i, j
                # Simulate the command string
                for c in s:
                    if c == 'L':
                        y -= 1
                    elif c == 'R':
                        y += 1
                    elif c == 'U':
                        x -= 1
                    elif c == 'D':
                        x += 1
                    # Check if the robot is still in the grid
                    if not (0 <= x < n and 0 <= y < m):
                        break
                else:
                    # If the robot didn't fall off the grid
                    safe = True
                    break
            if safe:
                break
        
        results.append("safe" if safe else "unsafe")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()