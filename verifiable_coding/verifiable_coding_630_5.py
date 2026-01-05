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
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            idx += 2
        
        # Check if all classes are present
        present = set(classes)
        if len(present) < k:
            results.append("-1")
            continue
        
        # Build the tree
        # Since it's a tree, we can do BFS or DFS to find the structure
        # We need to find the structure where each node has at most two outgoing edges
        # And each node (except root) has exactly one incoming edge
        # So it's a tree with root 1, and each node has at most two children
        
        # Build the tree structure
        tree = [[] for _ in range(n+1)]
        in_degree = [0] * (n+1)
        for u in range(1, n+1):
            for v in adj[u]:
                tree[u].append(v)
                in_degree[v] += 1
        
        # Check if the tree is valid (each node has at most two children)
        for u in range(1, n+1):
            if len(tree[u]) > 2:
                results.append("-1")
                break
        else:
            # Now find the minimum number of sparrows
            # We need to select at least one sparrow per class
            # We can use BFS to find the nodes that are in the same class as their parent
            # And select one node per class
            # We can use a greedy approach: select the node with the highest depth in the tree
            # Because that way we can cover more classes with fewer sparrows
            # We can use a BFS to find the depth of each node
            depth = [0] * (n+1)
            visited = [False] * (n+1)
            q = collections.deque()
            q.append(1)
            visited[1] = True
            while q:
                u = q.popleft()
                for v in tree[u]:
                    if not visited[v]:
                        visited[v] = True
                        depth[v] = depth[u] + 1
                        q.append(v)
            
            # Now, for each class, find the node with the maximum depth
            class_nodes = collections.defaultdict(list)
            for i in range(1, n+1):
                class_nodes[classes[i-1]].append(depth[i])
            
            # For each class, take the maximum depth node
            min_sparrows = 0
            for cls in range(1, k+1):
                if cls not in class_nodes:
                    results.append("-1")
                    break
                max_depth = max(class_nodes[cls])
                # We need to select a node in this class with depth >= max_depth
                # So we can select the node with max depth
                min_sparrows += 1
            else:
                results.append(str(min_sparrows))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()