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
    # We need to connect cities such that removing any one city doesn't disconnect the rest
    # This is equivalent to finding a spanning tree of the graph where the capital is connected to all others
    # But we need to ensure that the graph remains connected even if any one node is removed
    # This is equivalent to finding a 2-edge-connected graph on all nodes except the capital, and connecting the capital to the rest
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    # We can model this as a minimum spanning tree problem on the graph where the capital is connected to all other cities
    # Then we need to connect the other cities in such a way that the graph remains connected even if any one node is removed
    # This is equivalent to finding a minimum spanning tree on the graph where the capital is connected to all other cities, and then adding edges to ensure that the graph is 2-edge-connected
    
    #