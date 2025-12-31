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
        
        # Check if the command string is safe for any starting position
        safe = False
        
        # Try all possible starting positions
        for start_row in range(n):
            for start_col in range(m):
                row, col = start_row, start_col
                safe_path = True
                for c in s:
                    if c == 'L':
                        col -= 1
                    elif c == 'R':
                        col += 1
                    elif c == 'U':
                        row -= 1
                    elif c == 'D':
                        row += 1
                    # Check if the new position is outside the grid
                    if not (0 <= row < n and 0 <= col < m):
                        safe_path = False
                        break
                if safe_path:
                    safe = True
                    break
            if safe:
                break
        
        results.append("safe" if safe else "unsafe")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()