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
    
    room_info = []
    for _ in range(R):
        x = int(data[idx]); idx +=1
        y = int(data[idx]); idx +=1
        c1 = int(data[idx]); idx +=1
        c2 = int(data[idx]); idx +=1
        room_info.append((x, y, c1, c2))
    
    # Build adjacency list for cells
    grid = [[-1 for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            grid[x][y] = (x, y)
    
    # Find connected components (rooms)
    visited = [[False for _ in range(M)] for _ in range(N)]
    rooms = []
    
    def bfs(x, y):
        q = collections.deque()
        q.append((x, y))
        visited[x][y] = True
        room = []
        while q:
            cx, cy = q.popleft()
            room.append((cx, cy))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    # Check if there is a wall between (cx, cy) and (nx, ny)
                    # Check if the wall exists
                    found = False
                    for wall in walls:
                        x1, y1, x2, y2 = wall
                        if (x1 == cx and y1 == cy and x2 == nx and y2 == ny) or (x1 == nx and y1 == ny and x2 == cx and y2 == cy):
                            found = True
                            break
                    if not found:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return room
    
    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                room = bfs(x, y)
                rooms.append(room)
    
    # Map each cell to its room index
    cell_to_room = {}
    for i, room in enumerate(rooms):
        for x, y in room:
            cell_to_room[(x, y)] = i
    
    # Build adjacency between rooms
    room_adj = collections.defaultdict(list)
    for x1, y1, x2, y2 in walls:
        cell1 = (x1-1, y1-1)
        cell2 = (x2-1, y2-1)
        room1 = cell_to_room[cell1]
        room2 = cell_to_room[cell2]
        room_adj[room1].append(room2)
        room_adj[room2].append(room1)
    
    # Build room info
    room_info_dict = {}
    for x, y, c1, c2 in room_info:
        room = cell_to_room[(x-1, y-1)]
        room_info_dict[room] = (c1, c2)
    
    # DP: dp[i][j] = min cost to assign first i rooms to group 1 and j rooms to group 2
    # But since rooms are connected, we need to consider the cost of walls between rooms
    # Instead, we can model this as a graph where each node is a room, and edges represent walls between rooms
    # The cost of assigning a room to group 1 or 2 is the support cost for that group
    # The cost of walls between rooms depends on whether they are assigned to different groups
    
    # We can model this as a graph and find the minimum cost to assign rooms to groups such that adjacent rooms are not in different groups
    # This is equivalent to a graph partitioning problem, which can be solved with dynamic programming
    
    # However, for efficiency, we can use a dynamic programming approach with states for each room
    # But given the constraints, we can use a more efficient approach
    
    # We can model this as a graph and find the minimum cost to assign rooms to groups such that adjacent rooms are not in different groups
    # This is equivalent to finding a minimum cut in a graph
    
    # We can model this as a graph where each room is a node, and edges between rooms have a cost of K if they are assigned to different groups
    # The cost of assigning a room to group 1 or 2 is the support cost for that group
    
    # We can use a min-cut approach to find the minimum cost
    
    # Create a graph for min-cut
    # We create a source node and a sink node
    # For each room, we create an edge from source to room with capacity equal to the cost of assigning the room to group 1
    # We create an edge from room to sink with capacity equal to the cost of assigning the room to group 2
    # For each pair of adjacent rooms, we create an edge between them with capacity K (the cost of isolating the wall between them)
    
    # We then find the min-cut between source and sink, which gives the minimum cost
    
    # Implementing this requires a max-flow algorithm
    
    # We use the Dinic's algorithm for max-flow
    
    class Edge:
        def __init__(self, to, rev, capacity):
            self.to = to
            self.rev = rev
            self.capacity = capacity
    
    class MaxFlow:
        def __init__(self, N):
            self.size = N
            self.graph = [[] for _ in range(N)]
        
        def add_edge(self, fr, to, cap):
            forward = Edge(to, len(self.graph[to]), cap)
            backward = Edge(fr, len(self.graph[fr]), 0)
            self.graph[fr].append(forward)
            self.graph[to].append(backward)
        
        def bfs_level(self, s, t, level):
            queue = collections.deque()
            level[:] = [-1]*self.size
            level[s] = 0
            queue.append(s)
            while queue:
                v = queue.popleft()
                for edge in self.graph[v]:
                    if edge.capacity > 0 and level[edge.to] < 0:
                        level[edge.to] = level[v]+1
                        queue.append(edge.to)
                    if level[edge.to] >= 0 and edge.capacity > 0:
                        continue
            return level[t] != -1
        
        def dfs_flow(self, v, t, upTo, iter_, level):
            if v == t:
                return upTo
            for i in range(iter_[v], len(self.graph[v])):
                edge = self.graph[v][i]
                if edge.capacity > 0 and level[v] < level[edge.to]:
                    d = self.dfs_flow(edge.to, t, min(upTo, edge.capacity), iter_, level)
                    if d > 0:
                        edge.capacity -= d
                        self.graph[edge.to][edge.rev].capacity += d
                        return d
                iter_[v] += 1
            return 0
        
        def max_flow(self, s, t):
            flow = 0
            level = [-1]*self.size
            while self.bfs_level(s, t, level):
                iter_ = [0]*self.size
                while True:
                    f = self.dfs_flow(s, t, float('inf'), iter_, level)
                    if f == 0:
                        break
                    flow += f
                level = [-1]*self.size
            return flow
    
    # Create graph
    num_rooms = len(rooms)
    source = num_rooms
    sink = num_rooms + 1
    mf = MaxFlow(num_rooms + 2)
    
    # Add edges from source to rooms
    for i in range(num_rooms):
        c1, c2 = room_info_dict[i]
        mf.add_edge(source, i, c1)
        mf.add_edge(i, sink, c2)
    
    # Add edges between rooms
    for u in range(num_rooms):
        for v in room_adj[u]:
            if u < v:
                mf.add_edge(u, v, K)
                mf.add_edge(v, u, K)
    
    # Compute min-cut
    min_cut = mf.max_flow(source, sink)
    
    # The total cost is the sum of all support costs (since min-cut represents the minimum cost to assign rooms to groups)
    # The min-cut is the minimum cost to assign rooms to groups such that adjacent rooms are not in different groups
    # The total cost is the sum of all support costs, which is the sum of c1 and c2 for each room
    # But