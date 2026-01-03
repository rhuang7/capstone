import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        graph = [[] for _ in range(N + 1)]
        
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            graph[X].append(Y)
            graph[Y].append(X)
        
        # Perform BFS to find the order of stones based on levels
        # The level of a node is the depth in the BFS tree starting from node 1
        # The order is determined by the level and the order of traversal
        # We use a priority queue to ensure that nodes are processed in level order
        # and within the same level, nodes are processed in the order they were visited
        
        # Initialize BFS
        from collections import deque
        visited = [False] * (N + 1)
        queue = deque()
        queue.append(1)
        visited[1] = True
        level = [0] * (N + 1)
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[node] + 1
                    queue.append(neighbor)
        
        # The order is already level order, but we need to ensure that within the same level,
        # the nodes are ordered as per their traversal in BFS
        # Since BFS processes nodes in the order they are discovered, the order is correct
        
        # Output the order as space-separated values
        print(' '.join(map(str, order)))

if __name__ == '__main__':
    solve()