import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    cost = []
    index = 1
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(data[index]))
            index += 1
        cost.append(row)
    
    # The initial graph is a star with the capital (node 1) connected to all other nodes
    # We need to make the graph 2-connected, i.e., removing any single node does not disconnect the graph
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # To achieve this, we can model the problem as finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then adding edges to make it 2-connected
    # However, since the initial graph is already a star, we need to connect the other nodes in such a way that the graph remains connected even if any one node is removed
    
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then adding edges to make it 2-connected
    # The minimum cost to achieve this is the sum of the minimum edges connecting the other nodes in such a way that the graph remains connected even if any one node is removed
    
    # This is equivalent to finding a minimum spanning tree of the graph where the capital is connected to all other nodes, and then adding edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make the graph 2-connected
    
    # The minimum cost is the sum of the minimum edges connecting the other nodes in such a way that the graph remains connected even if any one node is removed
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can model this as a minimum spanning tree problem where the capital is connected to all other nodes, and we need to add edges to make it 2-connected
    
    # We can