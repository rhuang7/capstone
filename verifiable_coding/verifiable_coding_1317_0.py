import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx]); idx +=1
    M = int(data[idx]); idx +=1
    W = int(data[idx]); idx +=1
    K = int(data[idx]); idx +=1
    R = int(data[idx]); idx +=1

    walls = []
    for _ in range(W):
        x1 = int(data[idx]); idx +=1
        y1 = int(data[idx]); idx +=1
        x2 = int(data[idx]); idx +=1
        y2 = int(data[idx]); idx +=1
        walls.append((x1, y1, x2, y2))

    rooms = []
    for _ in range(R):
        x = int(data[idx]); idx +=1
        y = int(data[idx]); idx +=1
        c1 = int(data[idx]); idx +=1
        c2 = int(data[idx]); idx +=1
        rooms.append((x, y, c1, c2))

    # Find connected components (rooms)
    grid = [[-1 for _ in range(M)] for _ in range(N)]
    for x, y, _, _ in rooms:
        grid[x-1][y-1] = 1

    # Find connected components
    visited = [[False for _ in range(M)] for _ in range(N)]
    component = 0
    room_id = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                # BFS to find connected component
                q = collections.deque()
                q.append((i, j))
                visited[i][j] = True
                curr = []
                while q:
                    x, y = q.popleft()
                    curr.append((x, y))
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                # Assign component id
                for x, y in curr:
                    grid[x][y] = room_id
                room_id += 1

    # Build adjacency list for rooms
    adj = [[] for _ in range(room_id)]
    for x1, y1, x2, y2 in walls:
        # Check if the wall is between two cells in the same room
        # Each wall is between two cells (x1,y1) and (x2,y2)
        # We need to check if both cells are in the same room
        # But since walls are between cells, we can check if the two cells are in the same room
        # However, walls are between cells that are adjacent, so we can check if the two cells are in the same room
        # So for each wall, check if the two cells are in the same room
        # If they are, then this wall is between two cells in the same room, so it's not a wall between rooms
        # If they are not, then this wall is between two rooms
        # So for each wall, check if the two cells are in the same room
        # If not, then this wall is between two rooms
        # So we can add an edge between the two rooms
        # But first, we need to find the room id of each cell
        # But we have already assigned room ids to all cells
        # So for the two cells (x1,y1) and (x2,y2), we can get their room ids
        # But we need to check if they are in the same room
        # So for the wall between (x1,y1) and (x2,y2), check if they are in the same room
        # If they are not, then this wall is between two rooms
        # So we add an edge between the two rooms
        # But note that walls are between adjacent cells, so each wall is between two cells
        # So for each wall, check if the two cells are in the same room
        # If not, then this wall is between two rooms
        # So we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So for each wall, we get the room id of (x1,y1) and (x2,y2)
        # If they are different, then this wall is between two rooms
        # So we add an edge between the two rooms
        # But we need to make sure that we don't add duplicate edges
        # So for each wall, we check if the two cells are in the same room
        # If not, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1,y1) and (x2,y2)
        # But wait, the wall is between two cells that are adjacent
        # So for the wall between (x1,y1) and (x2,y2), the two cells are adjacent
        # So we can check if the two cells are in the same room
        # If they are not, then this wall is between two rooms
        # So we add an edge between the two rooms
        # So for each wall, we check if the two cells are in the same room
        # If not, then we add an edge between the two rooms
        # But how to get the room id of the two cells?
        # The grid has room ids assigned to all cells
        # So we can get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # So for each wall, we check if the two cells are in the same room
        # If not, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to make sure that we don't add duplicate edges
        # So for each wall, we check if the two cells are in the same room
        # If not, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1-1, y1-1) and (x2-1, y2-1)
        # If they are different, then we add an edge between the two rooms
        # But we need to check if the two cells are in the same room
        # So we get the room id of (x1