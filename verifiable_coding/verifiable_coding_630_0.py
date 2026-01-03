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
        
        # Check if the graph is a valid structure (each node has at most 2 outgoing edges, and in-degree is 1 except for root)
        valid = True
        for u in range(n):
            if len(graph[u]) > 2:
                valid = False
            if in_degree[u] > 1:
                valid = False
        if not valid:
            results.append(-1)
            continue
        
        # Check if the graph is a tree (connected and has n-1 edges)
        visited = [False] * n
        stack = [0]
        visited[0] = True
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        if sum(visited) != n:
            results.append(-1)
            continue
        
        # Check if the graph is a valid structure (each node has at most 2 outgoing edges, and in-degree is 1 except for root)
        # Already checked above
        
        # Check if all classes are present
        class_set = set(classes)
        if len(class_set) < k:
            results.append(-1)
            continue
        
        # Find all nodes with in-degree 1 (except root)
        root = 0
        nodes_with_in_degree_1 = []
        for i in range(n):
            if in_degree[i] == 1:
                nodes_with_in_degree_1.append(i)
        
        # Build the tree structure
        # Each node can have at most 2 children
        # We need to select sparrows such that every class is covered and every edge has at least one sparrow in either node
        
        # We need to find a way to select sparrows such that:
        # 1. Every class is represented in the selected sparrows
        # 2. For every edge (u, v), at least one of u or v is selected
        
        # We can model this as a problem where we need to select a subset of nodes such that:
        # - Every class is represented in the subset
        # - For every edge, at least one of the endpoints is in the subset
        
        # We can model this as a hitting set problem with constraints
        
        # Since k is small (up to 10), we can try all possible combinations of classes
        # For each class, we can try to select a node from that class to be a sparrow
        # But we need to ensure that for every edge, at least one of the endpoints is selected
        
        # We can use BFS to find the minimum number of sparrows needed
        
        # We can use a BFS approach where we track the classes covered and the nodes selected
        # However, since n is up to 2500 and k is up to 10, this approach may not be feasible
        
        # Instead, we can try to find the minimal number of sparrows by trying to select one node from each class
        # But we need to ensure that for every edge, at least one of the endpoints is selected
        
        # We can try all possible combinations of selecting one node from each class
        # Since k is small, this is feasible
        
        # However, we need to ensure that for every edge, at least one of the endpoints is selected
        
        # We can try to find the minimal number of sparrows by trying all possible combinations of selecting one node from each class
        # and checking if the selected nodes cover all edges
        
        # Let's try this approach
        
        class_to_nodes = {}
        for i in range(n):
            c = classes[i]
            if c not in class_to_nodes:
                class_to_nodes[c] = []
            class_to_nodes[c].append(i)
        
        # Try all possible combinations of selecting one node from each class
        from itertools import product
        
        min_sparrows = float('inf')
        for combo in product(*[class_to_nodes[c] for c in range(1, k+1)]):
            # Check if this combo covers all edges
            covered = True
            for u, v in edges:
                if combo[u] != u and combo[v] != v:
                    covered = False
                    break
            if covered:
                min_sparrows = min(min_sparrows, len(combo))
        
        if min_sparrows == float('inf'):
            results.append(-1)
        else:
            results.append(min_sparrows)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()