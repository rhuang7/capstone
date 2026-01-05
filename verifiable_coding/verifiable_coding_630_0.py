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
        
        # Build graph
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Check if the graph is a valid tree with root 0 (soldier 1)
        if len(graph) != n or in_degree[0] != 0:
            results.append(-1)
            continue
        
        # Check if the graph is a valid tree with root 0 and each node has at most 2 outgoing edges
        visited = [False] * n
        queue = [0]
        visited[0] = True
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                if visited[v]:
                    results.append(-1)
                    break
                visited[v] = True
                queue.append(v)
            else:
                continue
            break
        
        if len(visited) != n:
            results.append(-1)
            continue
        
        # Check if the graph is a valid tree with root 0 and each node has at most 2 outgoing edges
        for u in range(n):
            if len(graph[u]) > 2:
                results.append(-1)
                break
        else:
            # Find the classes
            class_count = collections.defaultdict(int)
            for c in classes:
                class_count[c] += 1
            
            # If any class is missing, it's impossible
            for c in range(1, k+1):
                if class_count.get(c, 0) == 0:
                    results.append(-1)
                    break
            else:
                # Find the minimum number of sparrows
                # We need to select at least one soldier from each class
                # But we can select a soldier from a class if it is a leaf node
                # So we need to find all leaves and see which classes they belong to
                # Then select one soldier from each class that is a leaf
                # If a class has no leaf, it's impossible
                leaves = []
                for i in range(n):
                    if len(graph[i]) == 0:
                        leaves.append(i)
                
                # Check if each class has at least one leaf
                class_leaves = collections.defaultdict(list)
                for i in leaves:
                    class_leaves[classes[i]].append(i)
                
                for c in range(1, k+1):
                    if not class_leaves.get(c, []):
                        results.append(-1)
                        break
                else:
                    # We can select one leaf from each class
                    # The minimum number of sparrows is the number of classes
                    results.append(k)
        
    for res in results:
        print(res)