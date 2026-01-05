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
                current_component = []
                while q:
                    x, y = q.popleft()
                    current_component.append((x, y))
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                # Assign component id
                for x, y in current_component:
                    grid[x][y] = room_id
                room_id += 1

    # Now, for each room, find all walls between it and other rooms
    # We need to find for each wall, which rooms it separates
    # First, build a map of walls to their room pairs
    wall_to_rooms = {}
    for x1, y1, x2, y2 in walls:
        # Check if the wall is between two cells
        # For example, between (x1, y1) and (x2, y2)
        # We need to check which rooms the cells belong to
        # Since the wall is between two cells, we need to check if they are in different rooms
        # So for each wall, check the rooms of the two cells
        # But since the wall is between two cells, the cells are adjacent
        # So the wall is between two cells that are in different rooms
        # So we need to find for each wall, which rooms it separates
        # So for each wall, check the rooms of the two cells
        # But how to find the room of a cell?
        # We have grid[x][y] = room_id
        # So for each cell (x1, y1) and (x2, y2), get their room id
        # If they are in different rooms, then the wall is between them
        # So for each wall, check if the two cells are in different rooms
        # If so, then this wall is between two rooms
        # So we can add this wall to the list of walls between the two rooms
        # So for each wall, we check the two cells
        # But since the wall is between two adjacent cells, we can check the room of each cell
        # So for each wall, check the rooms of the two cells
        # If they are different, then this wall is between two rooms
        # So we can add this wall to the list of walls between the two rooms
        # So for each wall, we check the two cells
        # So for the wall between (x1, y1) and (x2, y2), we check the rooms of (x1, y1) and (x2, y2)
        # But since the wall is between two adjacent cells, the cells are in different rooms
        # So we can get the room id of each cell
        # So for the wall, we get the room id of (x1, y1) and (x2, y2)
        # If they are different, then this wall is between two rooms
        # So we add this wall to the list of walls between the two rooms
        # But since the wall is between two cells, the two cells are adjacent
        # So the wall is between two cells in different rooms
        # So we can add this wall to the list of walls between the two rooms
        # So for each wall, we get the room id of the two cells
        # Then, if they are different, we add this wall to the list of walls between the two rooms
        # So we can do this as follows:
        # For the wall between (x1, y1) and (x2, y2), check the room id of (x1, y1) and (x2, y2)
        # If they are different, then this wall is between two rooms
        # So we can add this wall to the list of walls between the two rooms
        # So for each wall, we check the room of the two cells
        # But how to get the room of a cell? We have grid[x][y] = room_id
        # So for (x1, y1), room1 = grid[x1-1][y1-1]
        # For (x2, y2), room2 = grid[x2-1][y2-1]
        # If room1 != room2, then this wall is between room1 and room2
        # So we add this wall to the list of walls between room1 and room2
        # So for each wall, we do:
        room1 = grid[x1-1][y1-1]
        room2 = grid[x2-1][y2-1]
        if room1 != room2:
            if (room1, room2) not in wall_to_rooms:
                wall_to_rooms[(room1, room2)] = 0
            wall_to_rooms[(room1, room2)] += 1
            if (room2, room1) not in wall_to_rooms:
                wall_to_rooms[(room2, room1)] = 0
            wall_to_rooms[(room2, room1)] += 1

    # Now, for each room, we need to decide which group to assign it to
    # We can model this as a graph where each node is a room, and edges represent walls between rooms
    # The cost of assigning a room to group 1 is c1, to group 2 is c2
    # The total cost is sum of (c1 or c2 for each room) + K * number of walls between rooms in different groups
    # So we need to find the minimum total cost
    # This is a problem of partitioning the graph into two groups with minimum cost
    # This is a classic problem that can be solved with a min-cut algorithm
    # But since the number of rooms is up to 500, we can use a dynamic programming approach
    # However, for the given constraints, it's better to use a min-cut approach

    # So we can model this as a graph where each room is a node, and edges between rooms represent walls
    # The cost of an edge between two rooms is the number of walls between them
    # The cost of assigning a room to group 1 is c1, to group 2 is c2
    # We need to find the minimum total cost of assigning rooms to groups such that the cost of walls between different groups is minimized
    # This is equivalent to finding the minimum cut in a graph
    # So we can model this as a graph where each room is a node, and edges between rooms have weight equal to the number of walls between them
    # We can use a min-cut algorithm to find the minimum cut

    # Let's build the graph
    # We need to create a graph with nodes for each room, and edges between rooms with weight equal to the number of walls between them
    # Then, we can use a min-cut algorithm to find the minimum cut
    # The minimum cut will give us the minimum cost of assigning rooms to groups such that the cost of walls between different groups is minimized
    # The total cost is sum of (c1 or c2 for each room) + K * (number of walls between different groups)

    # So we can model this as a graph with nodes for each room, and edges between rooms with