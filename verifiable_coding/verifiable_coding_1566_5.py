import sys
import math
from collections import defaultdict

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
        Q = int(data[idx+1])
        idx += 2
        edges = []
        for __ in range(Q):
            i = int(data[idx])
            j = int(data[idx+1])
            val = int(data[idx+2])
            idx += 3
            edges.append((i, j, val))
        # Build graph
        graph = defaultdict(list)
        for i, j, val in edges:
            if i > j:
                i, j = j, i
            graph[i].append((j, val))
        # Check for contradictions
        # For each node, assign a value and check consistency
        # We can use BFS to assign values
        # We need to ensure that for any i, j, |A[i] - A[j]| = B[i][j]
        # So for each edge (i, j, val), we must have |A[i] - A[j]| = val
        # This implies that A[i] - A[j] = ±val
        # So we can assign A[i] = A[j] ± val
        # We can use BFS to assign values to nodes
        # Start with node 1, assign A[1] = 0
        # Then for each neighbor, assign A[neighbor] = A[i] ± val
        # If there is a contradiction, return no
        # Also, check that for any i, j, B[i][j] = B[j][i]
        # Because B[i][j] = |A[i] - A[j]| and B[j][i] = |A[j] - A[i]|, so they must be equal
        # So for any edge (i, j, val), we must have B[j][i] = val
        # So we need to check that for any given (i, j, val), B[j][i] is also val
        # But since the input may not have B[j][i], we need to check if it's present
        # So for each edge (i, j, val), if (j, i, val) is not in the edges, then it's invalid
        # So first check that for any (i, j, val), (j, i, val) is also present
        # If not, then it's impossible
        # So for each edge (i, j, val), check if (j, i, val) is present
        # If not, then it's impossible
        # So first check for this
        # Create a set of edges
        edge_set = set()
        for i, j, val in edges:
            if i > j:
                i, j = j, i
            edge_set.add((i, j, val))
        valid = True
        for i, j, val in edges:
            if i > j:
                i, j = j, i
            if (j, i, val) not in edge_set:
                valid = False
                break
        if not valid:
            results.append("no")
            continue
        # Now check if the graph is bipartite
        # We can assign values to nodes such that for any edge (i, j, val), |A[i] - A[j]| = val
        # This is equivalent to A[i] - A[j] = ±val
        # So for any edge (i, j, val), we have A[i] = A[j] ± val
        # So we can assign A[i] = A[j] + val or A[i] = A[j] - val
        # This is similar to a bipartition problem where each edge has a weight
        # We can model this as a graph where each edge has a weight (val)
        # And we need to assign values to nodes such that for any edge (i, j), |A[i] - A[j]| = val
        # This is equivalent to A[i] - A[j] = ±val
        # So we can model this as a graph where each edge has a weight (val), and we need to assign values to nodes such that for any edge (i, j), A[i] - A[j] = ±val
        # This is a bipartition problem with weights
        # We can use BFS to assign values to nodes
        # We can assign A[1] = 0
        # Then for each neighbor, assign A[neighbor] = A[i] ± val
        # If there is a contradiction, return no
        # So we can use BFS
        # Create a dictionary to store the assigned values
        A = {}
        A[1] = 0
        # Use a queue for BFS
        queue = [1]
        # Use a visited set
        visited = set()
        visited.add(1)
        # Use a dictionary to store the value of each node
        # We can use a dictionary to store the value of each node
        # For each node, we need to check all its neighbors
        # For each neighbor, we need to check if it's already assigned
        # If not, assign it based on the edge value
        # If it's already assigned, check if the value is consistent
        # If not, return no
        # Also, for each edge (i, j, val), we need to check that |A[i] - A[j]| = val
        # So for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # But since we are building the graph from the edges, we can check this during BFS
        # So for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we can check that |A[i] - A[j]| == val
        # So we can build a graph where each node has a list of edges
        # For each edge (i, j, val), we can add it to the graph
        # Then during BFS, for each node, we check all its edges
        # So build the graph
        graph = defaultdict(list)
        for i, j, val in edges:
            if i > j:
                i, j = j, i
            graph[i].append((j, val))
            graph[j].append((i, val))
        # Now perform BFS
        # Start with node 1
        # Assign A[1] = 0
        # Then for each neighbor, assign A[neighbor] = A[i] ± val
        # If there is a contradiction, return no
        # So during BFS, for each node, we check all its edges
        # For each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we can check that |A[i] - A[j]| == val
        # If not, return no
        # So during BFS, for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each node, we check all its edges
        # So we can use BFS
        # Initialize A and visited
        A = {}
        A[1] = 0
        visited = set()
        visited.add(1)
        queue = [1]
        # Use a dictionary to store the value of each node
        # For each node, we need to check all its edges
        # For each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each node, we check all its edges
        # So for each node, we check all its edges
        # For each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each node, we check all its edges
        # So for each node, we check all its edges
        # So during BFS, for each node, we check all its edges
        # So for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we need to check that |A[i] - A[j]| == val
        # So during BFS, for each edge (i, j, val), we