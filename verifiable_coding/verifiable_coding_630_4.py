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
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        
        # Check if the graph is a valid tree with the required properties
        # Each node has at most two outgoing edges
        for u in range(n):
            if len(graph[u]) > 2:
                results.append(-1)
                break
        else:
            # Check if the tree is connected and starts from node 0 (soldier 1)
            visited = [False] * n
            stack = [0]
            visited[0] = True
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            if not all(visited):
                results.append(-1)
                continue
            
            # Check if each node (except 0) has exactly one incoming edge
            in_degree = [0] * n
            for u in range(n):
                for v in graph[u]:
                    in_degree[v] += 1
            for i in range(1, n):
                if in_degree[i] != 1:
                    results.append(-1)
                    break
            else:
                # Now, find the minimum number of sparrows
                # Each class must have at least one sparrow
                class_present = set(classes)
                if len(class_present) < k:
                    results.append(-1)
                    continue
                
                # We need to select at least one soldier from each class
                # We can choose soldiers from the end of the tree (leaves)
                # Because each node has at most two children, the tree is a DAG
                # We can perform a post-order traversal and select the last node of each class
                
                # Build the tree as a DAG
                # We'll use a parent array to find the children of each node
                parent = [-1] * n
                for u in range(n):
                    for v in graph[u]:
                        if parent[v] == -1 and v != 0:
                            parent[v] = u
                
                # Perform a post-order traversal to find the last occurrence of each class
                class_last = {}
                visited = [False] * n
                stack = [(0, False)]
                while stack:
                    node, processed = stack.pop()
                    if processed:
                        cls = classes[node]
                        if cls in class_last:
                            class_last[cls] = max(class_last[cls], node)
                        else:
                            class_last[cls] = node
                        continue
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack.append((node, True))
                    for child in graph[node]:
                        if parent[child] == node:
                            stack.append((child, False))
                
                # Check if all classes have at least one node in the class_last
                if len(class_last) < k:
                    results.append(-1)
                    continue
                
                # The minimum number of sparrows is the number of classes
                results.append(k)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()