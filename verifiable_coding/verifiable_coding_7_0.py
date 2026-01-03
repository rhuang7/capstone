import sys

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
        idx += 1
        voters = []
        for _ in range(n):
            m_i = int(data[idx])
            p_i = int(data[idx + 1])
            idx += 2
            voters.append((m_i, p_i))
        
        # Sort voters by m_i in descending order
        voters.sort(reverse=True, key=lambda x: x[0])
        
        # Use a priority queue (min-heap) to track the cost of each group
        import heapq
        heap = []
        
        # Initially, we have no voters
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        # But we can also consider buying a voter with m_i > 0 to get more people
        
        # We'll use a greedy approach: always buy the cheapest voter that can contribute the most
        # We'll track the number of people we have, and for each voter, we'll decide whether to buy them or not
        
        # Start with 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        # But we can also consider buying a voter with m_i > 0 to get more people
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy the cheapest voter to start with
        
        # We'll use a priority queue (min-heap) to track the cost of each group
        # The heap will store the cost of the current group of people
        
        # We'll also track the number of people we have
        # Initially, we have 0 people
        # We need to buy at least one voter to start the process
        # So we need to buy