import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    idx = 1
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        top = data[idx]
        idx += 1
        bottom = data[idx]
        idx += 1
        
        # Convert to list of integers
        top = [int(c) for c in top]
        bottom = [int(c) for c in bottom]
        
        # Directions: 0 - right, 1 - down, 2 - left, 3 - up
        # We'll use BFS to find a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array with directions
        
        # Initialize the grid with directions
        grid = [[0]*n for _ in range(2)]
        
        # Function to get direction from pipe type
        def get_dir(pipe):
            if pipe == 1 or pipe == 2:
                return 0  # straight right
            elif pipe == 3 or pipe == 4:
                return 1  # straight down
            elif pipe == 5 or pipe == 6:
                return 2  # straight left
            else:
                return 3  # straight up
        
        # Set initial directions
        grid[0][0] = get_dir(top[0])
        grid[1][n-1] = get_dir(bottom[n-1])
        
        # BFS
        from collections import deque
        visited = [[False]*n for _ in range(2)]
        q = deque()
        q.append((0, 0, 0))  # (row, col, direction)
        visited[0][0] = True
        
        found = False
        
        while q:
            r, c, d = q.popleft()
            
            # Check if we reached the end
            if r == 1 and c == n-1:
                found = True
                break
            
            # Try to move in the current direction
            if d == 0:  # right
                if c + 1 < n:
                    if not visited[0][c+1]:
                        visited[0][c+1] = True
                        q.append((0, c+1, 0))
            elif d == 1:  # down
                if r + 1 < 2:
                    if not visited[1][c]:
                        visited[1][c] = True
                        q.append((1, c, 1))
            elif d == 2:  # left
                if c - 1 >= 0:
                    if not visited[0][c-1]:
                        visited[0][c-1] = True
                        q.append((0, c-1, 2))
            elif d == 3:  # up
                if r - 1 >= 0:
                    if not visited[0][c]:
                        visited[0][c] = True
                    if not visited[1][c]:
                        visited[1][c] = True
                    q.append((0, c, 3))
            
            # Try to turn 90 degrees clockwise
            new_d = (d + 1) % 4
            if r == 0:
                if c + 1 < n:
                    if not visited[0][c+1]:
                        visited[0][c+1] = True
                        q.append((0, c+1, new_d))
            elif r == 1:
                if c - 1 >= 0:
                    if not visited[1][c-1]:
                        visited[1][c-1] = True
                        q.append((1, c-1, new_d))
            
            # Try to turn 90 degrees counterclockwise
            new_d = (d - 1) % 4
            if r == 0:
                if c - 1 >= 0:
                    if not visited[0][c-1]:
                        visited[0][c-1] = True
                        q.append((0, c-1, new_d))
            elif r == 1:
                if c + 1 < n:
                    if not visited[1][c+1]:
                        visited[1][c+1] = True
                        q.append((1, c+1, new_d))
        
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()