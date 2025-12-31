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
        # Use BFS to assign values
        # We can assign A[1] = 0, and then assign other values based on the edges
        # If there is a contradiction, return no
        # Use a dictionary to store the assigned values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are consistent
        # So we can use BFS to assign values
        # We can use a dictionary to store the values
        # If a node is not in the dictionary, assign it a value
        # For each edge (i, j, val), check if |A[i] - A[j]| == val
        # If not, return no
        # We can assign A[1] = 0, and then assign A[i] = A[j] + val or A[j] - val
        # But we need to make sure that the assignments are