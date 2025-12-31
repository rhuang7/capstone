import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+M]))
            matrix.append(row)
            idx += M
        S = data[idx]
        idx += 1
        P = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        
        # Precompute the number of steps for each cell
        steps = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                steps[i][j] = i + j
        
        # Precompute the required character for each cell along all paths
        # We'll use Dijkstra's algorithm to find the minimum cost path
        # Each state is (cost, i, j, required_char)
        # We'll use a priority queue to find the minimum cost path
        
        # Initialize the priority queue
        pq = []
        # The starting point is (0, 0, 0) with required character S[0]
        # We need to check if the starting cell matches the required character
        # or if we need to change it
        start_char = S[0]
        cost = 0
        if matrix[0][0] == start_char:
            cost = 0
        else:
            cost = P
        heapq.heappush(pq, (cost, 0, 0, 0))
        
        # Visited array to track the minimum cost to reach each cell with a certain required character
        # Since the required character is determined by the path, we need to track it
        # We'll use a 3D array: visited[i][j][k], where k is 0 or 1 (required character)
        # But since the required character is determined by the path, we can track it as part of the state
        # So we'll use a 2D array of dictionaries: visited[i][j] = {0: cost, 1: cost}
        visited = [[dict() for _ in range(M)] for _ in range(N)]
        
        while pq:
            cost, i, j, required_char = heapq.heappop(pq)
            
            # If we've reached the end, return the cost
            if i == N-1 and j == M-1:
                results.append(cost)
                break
            
            # Check if we've already visited this cell with this required character
            if required_char in visited[i][j]:
                if visited[i][j][required_char] <= cost:
                    continue
            
            # Mark this state as visited
            visited[i][j][required_char] = cost
            
            # Try moving right
            if j + 1 < M:
                new_j = j + 1
                new_steps = steps[i][new_j]
                new_char = S[new_steps]
                # Calculate the cost to change the cell or not
                if matrix[i][new_j] == new_char:
                    new_cost = cost
                else:
                    new_cost = cost + P
                heapq.heappush(pq, (new_cost, i, new_j, new_char))
            
            # Try moving down
            if i + 1 < N:
                new_i = i + 1
                new_j = j
                new_steps = steps[new_i][new_j]
                new_char = S[new_steps]
                # Calculate the cost to change the cell or not
                if matrix[new_i][new_j] == new_char:
                    new_cost = cost
                else:
                    new_cost = cost + P
                heapq.heappush(pq, (new_cost, new_i, new_j, new_char))
        
        # If we didn't reach the end, it means there's no valid path, but according to the problem statement, there is one
        # So we can assume that the loop will have found a solution
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()