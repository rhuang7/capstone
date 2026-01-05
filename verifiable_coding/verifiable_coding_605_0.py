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
        
        # Check if the command string can be executed safely from any starting position
        safe = False
        for start_row in range(n):
            for start_col in range(m):
                row, col = start_row, start_col
                safe_path = True
                for move in s:
                    if move == 'L':
                        col -= 1
                    elif move == 'R':
                        col += 1
                    elif move == 'U':
                        row -= 1
                    elif move == 'D':
                        row += 1
                    # Check if the robot is still inside the grid
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