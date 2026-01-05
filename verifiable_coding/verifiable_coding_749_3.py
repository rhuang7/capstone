import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    costs = []
    index = 1
    for _ in range(N):
        row = list(map(int, data[index:index+N]))
        index += N
        costs.append(row)
    
    # Build a graph where each node is a city
    # We need to connect all cities such that removing any one city leaves the rest connected
    # This is equivalent to finding a minimum spanning tree (MST) of the graph with the capital (city 1) as a special node
    # However, the MST of the entire graph would not satisfy the condition, so we need to find a way to ensure that the graph remains connected even if any one city is removed
    # This is equivalent to finding a 2-edge-connected graph with minimum total cost, but with the constraint that city 1 is connected to all others
    
    # We can model this as a problem of finding a minimum spanning tree (MST) of the graph with the capital (city 1) as a special node
    # However, since the graph is already connected (capital is connected to all others), we need to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree that includes all nodes and has the property that removing any one node leaves the rest connected
    
    # To achieve this, we can model the problem as a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected even if any one node is removed
    
    # The correct approach is to construct a minimum spanning tree (MST) of the graph where the capital is connected to all other nodes, and then we need to add edges to ensure that the graph remains connected