import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+M]))
        idx += M
        
        # Initialize flavor availability
        flavor_available = [c for c in C]
        # For each flavor, store a max heap of (B_i, D_i)
        flavor_bheap = [[] for _ in range(M)]
        
        for i in range(N):
            D_i = int(data[idx]) - 1
            F_i = int(data[idx+1])
            B_i = int(data[idx+2])
            idx += 3
            heapq.heappush(flavor_bheap[D_i], (-B_i, D_i))  # Use negative for max heap
        
        # For each flavor, keep track of available counts
        # And for each flavor, keep track of the best B_i options
        # We'll use a priority queue for each flavor to get the best B_i options
        
        # Now process each customer
        profit = 0
        flavor_choices = []
        
        for i in range(N):
            D_i = int(data[idx]) - 1
            F_i = int(data[idx+1])
            B_i = int(data[idx+2])
            idx += 3
            
            # Check if we can give the favorite flavor
            if flavor_available[D_i] > 0:
                profit += F_i
                flavor_available[D_i] -= 1
                flavor_choices.append(D_i + 1)
                continue
            
            # Else, we need to choose another flavor
            # Find the flavor with the highest B_i available
            best_b = -1
            best_flavor = -1
            for j in range(M):
                if flavor_available[j] > 0:
                    # Get the best B_i for this flavor
                    if flavor_bheap[j]:
                        current_b = -flavor_bheap[j][0][0]
                        if current_b > best_b:
                            best_b = current_b
                            best_flavor = j
            if best_flavor != -1:
                profit += best_b
                flavor_available[best_flavor] -= 1
                flavor_choices.append(best_flavor + 1)
            else:
                # This should not happen as per problem constraints
                pass
        
        results.append(str(profit))
        results.append(' '.join(map(str, flavor_choices)))
    
    print('\n'.join(results))