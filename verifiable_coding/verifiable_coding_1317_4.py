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
    
    # Initialize grid
    grid = [[-1 for _ in range(M)] for _ in range(N)]
    
    # Build adjacency list for rooms
    adj = collections.defaultdict(list)
    
    # Read walls
    for _ in range(W):
        x1 = int(data[idx])-1; idx +=1
        y1 = int(data[idx])-1; idx +=1
        x2 = int(data[idx])-1; idx +=1
        y2 = int(data[idx])-1; idx +=1
        
        # Check if cells are adjacent
        if (abs(x1 - x2) + abs(y1 - y2)) == 1:
            # Add wall between cells
            # For each cell, add an edge to the other
            adj[(x1, y1)].append((x2, y2))
            adj[(x2, y2)].append((x1, y1))
    
    # Find connected components (rooms)
    visited = [[False for _ in range(M)] for _ in range(N)]
    rooms = []
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                # BFS to find room
                q = collections.deque()
                q.append((i, j))
                visited[i][j] = True
                room = []
                while q:
                    x, y = q.popleft()
                    room.append((x, y))
                    for nx, ny in adj[(x, y)]:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                rooms.append(room)
    
    # Read support costs
    support = {}
    for _ in range(R):
        x = int(data[idx])-1; idx +=1
        y = int(data[idx])-1; idx +=1
        c1 = int(data[idx]); idx +=1
        c2 = int(data[idx]); idx +=1
        support[(x, y)] = (c1, c2)
    
    # For each room, find the best assignment (group 1 or group 2)
    # We'll use dynamic programming to find the minimum cost
    # Let dp[i] be the minimum cost for the first i rooms
    # We'll track for each room which group it is assigned to
    
    # First, for each room, compute the cost if assigned to group 1 or group 2
    room_costs = []
    for room in rooms:
        min_cost = float('inf')
        for (x, y) in room:
            c1, c2 = support[(x, y)]
            min_cost = min(min_cost, c1, c2)
        room_costs.append(min_cost)
    
    # Now, we need to compute the cost of walls between rooms
    # We'll need to find all adjacent rooms
    # For each cell in a room, check its neighbors and see if they belong to another room
    # We'll need to map each cell to its room index
    cell_to_room = {}
    for i in range(N):
        for j in range(M):
            for room in rooms:
                if (i, j) in room:
                    cell_to_room[(i, j)] = rooms.index(room)
                    break
    
    # Now, find all adjacent room pairs
    adjacent_rooms = set()
    for i in range(N):
        for j in range(M):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    if (i, j) in cell_to_room and (ni, nj) in cell_to_room:
                        r1 = cell_to_room[(i, j)]
                        r2 = cell_to_room[(ni, nj)]
                        if r1 != r2:
                            adjacent_rooms.add((r1, r2))
                            adjacent_rooms.add((r2, r1))
    
    # Now, we need to assign each room to group 1 or group 2, such that adjacent rooms are not both assigned to the same group
    # This is a graph problem where we need to assign colors to nodes such that adjacent nodes have different colors
    # We can model this as a graph and use dynamic programming
    
    # We'll use DP with states: dp[i][0] = min cost for first i rooms, with room i assigned to group 1
    # dp[i][1] = min cost for first i rooms, with room i assigned to group 2
    
    # Initialize DP
    dp = [[float('inf')] * 2 for _ in range(len(rooms))]
    dp[0][0] = room_costs[0]
    dp[0][1] = room_costs[0]
    
    for i in range(1, len(rooms)):
        # For each room, check which rooms it is adjacent to
        adj_rooms = []
        for r in range(len(rooms)):
            if (i, r) in adjacent_rooms:
                adj_rooms.append(r)
        
        # For current room i, check if it can be assigned to group 1 or group 2
        # If it can be assigned to group 1, then all adjacent rooms must be assigned to group 2
        # Similarly for group 2
        
        # Compute cost for group 1
        cost1 = room_costs[i]
        for r in adj_rooms:
            if dp[r][0] == float('inf'):
                cost1 = float('inf')
                break
            cost1 += dp[r][1]
        dp[i][0] = cost1
        
        # Compute cost for group 2
        cost2 = room_costs[i]
        for r in adj_rooms:
            if dp[r][1] == float('inf'):
                cost2 = float('inf')
                break
            cost2 += dp[r][0]
        dp[i][1] = cost2
    
    # Now, compute the total cost
    # We also need to compute the cost of walls between rooms
    # For each adjacent room pair, if they are assigned to different groups, add K * number of walls between them
    
    # First, compute the number of walls between each room pair
    # We'll need to count how many walls are between two rooms
    # For each wall, check if it is between two rooms
    # We'll need to map each wall to the room indices it separates
    
    # Create a list of walls
    walls = []
    for _ in range(W):
        x1 = int(data[idx])-1; idx +=1
        y1 = int(data[idx])-1; idx +=1
        x2 = int(data[idx])-1; idx +=1
        y2 = int(data[idx])-1; idx +=1
        walls.append(((x1, y1), (x2, y2)))
    
    # For each wall, check which rooms it separates
    wall_room_pairs = []
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        r1 = cell_to_room[(x1, y1)]
        r2 = cell_to_room[(x2, y2)]
        if r1 != r2:
            wall_room_pairs.append((r1, r2))
    
    # Now, compute the total cost
    total_cost = 0
    for i in range(len(rooms)):
        for j in range(i + 1, len(rooms)):
            if (i, j) in adjacent_rooms:
                # Check if they are assigned to different groups
                if (dp[i][0] != float('inf') and dp[j][1] != float('inf') and dp[i][0] + dp[j][1] == dp[i][0] + dp[j][1]):
                    total_cost += K
                elif (dp[i][1] != float('inf') and dp[j][0] != float('inf') and dp[i][1] + dp[j][0] == dp[i][1] + dp[j][0]):
                    total_cost += K
    
    # The minimum cost is the minimum of the two possible assignments for the last room
    min_total = min(dp[-1][0], dp[-1][1])
    min_total += total_cost
    print(min_total)

if __name__ == '__main__':
    solve()