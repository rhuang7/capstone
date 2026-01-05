import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        classes = list(map(int, data[idx:idx+n]))
        idx += n
        edges = []
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Build the graph
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Check if the graph is a valid tree with the given constraints
        # Each node has at most two outgoing edges
        for u in range(n):
            if len(graph[u]) > 2:
                results.append(-1)
                break
        else:
            # Check if the graph is a tree with root 0 (soldier 1)
            visited = [False] * n
            queue = [0]
            visited[0] = True
            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            if not all(visited):
                results.append(-1)
                continue
            
            # Check if each node (except 0) has exactly one incoming edge
            for i in range(1, n):
                if in_degree[i] != 1:
                    results.append(-1)
                    break
            else:
                # Now, find the minimum number of sparrows
                # We need to select at least one soldier from each class
                class_count = collections.defaultdict(int)
                for c in classes:
                    class_count[c] += 1
                
                # We need to select at least one soldier from each class
                # So, we need to find a set of soldiers such that:
                # 1. Each class has at least one soldier in the set
                # 2. The soldiers form a valid tree structure (each node has at most two outgoing edges)
                # 3. The set is minimal in size
                
                # We can use BFS to find the minimum number of sparrows
                # We need to select at least one soldier from each class
                # So, we can perform a BFS where we track which classes are covered
                # The state is (current_node, covered_classes)
                # We can use a priority queue to find the minimum number of sparrows
                # Since k is small (<=10), we can represent covered_classes as a bitmask
                # The maximum number of classes is 10, so the bitmask can be up to 2^10 = 1024
                
                # We can use BFS to find the minimum number of sparrows
                from collections import deque
                visited = [False] * (1 << k)
                q = deque()
                # Start from node 0 (soldier 1)
                # Check if it belongs to any class
                class_of_0 = classes[0]
                mask = 1 << (class_of_0 - 1)
                q.append((0, mask))
                visited[mask] = True
                min_sparrows = float('inf')
                
                while q:
                    node, mask = q.popleft()
                    # If all classes are covered
                    if mask == (1 << k) - 1:
                        min_sparrows = min(min_sparrows, bin(mask).count('1'))
                        continue
                    # Try to select this node as a sparrow
                    # Check if this node's class is already covered
                    class_of_node = classes[node]
                    new_mask = mask
                    if not (mask & (1 << (class_of_node - 1))):
                        new_mask |= (1 << (class_of_node - 1))
                    if new_mask != mask:
                        if not visited[new_mask]:
                            visited[new_mask] = True
                            q.append((node, new_mask))
                    # Try to go to children
                    for child in graph[node]:
                        if not visited[mask]:
                            visited[mask] = True
                            q.append((child, mask))
                
                if min_sparrows != float('inf'):
                    results.append(min_sparrows)
                else:
                    results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()