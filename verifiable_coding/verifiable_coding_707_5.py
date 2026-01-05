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
        # The level of a node is determined by the depth in the BFS tree
        # Since the mountain structure is such that each level i can have at most 2^i stones
        # We can use BFS to determine the order of nodes based on their level
        # The order will be such that nodes at lower levels come first
        
        visited = [False] * (N + 1)
        q = [1]
        visited[1] = True
        level = [0] * (N + 1)
        order = []
        
        while q:
            node = q.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    level[neighbor] = level[node] + 1
                    q.append(neighbor)
        
        # The order is determined by BFS, which ensures nodes at lower levels come first
        # But the problem says that the sequence must be non-decreasing, which implies that
        # the order is based on the level of the node, and within the same level, the order
        # is determined by the order in which they were visited (which is BFS order)
        # However, the problem's example shows that the output is the actual stone numbers
        # in the order they were visited, which is the BFS order
        
        # So the output is simply the order in which nodes were visited in BFS
        print(' '.join(map(str, order)))

if __name__ == '__main__':
    solve()