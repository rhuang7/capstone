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
        # For each flavor, store the customers who prefer it
        flavor_customers = [[] for _ in range(M)]
        # For each flavor, store the best B_i for customers who can't get their favorite
        # We'll use a max-heap for B_i (using negative values for min-heap)
        flavor_b_heap = [[] for _ in range(M)]
        
        for i in range(N):
            D_i = int(data[idx]) - 1  # 0-based
            F_i = int(data[idx+1])
            B_i = int(data[idx+2])
            idx += 3
            
            flavor_customers[D_i].append((F_i, B_i))
            # For the flavor, we want to keep the best B_i for when we can't serve the favorite
            # We use a max-heap (using negative values for min-heap)
            heapq.heappush(flavor_b_heap[D_i], (-B_i, B_i))
        
        # For each flavor, sort the customers by F_i (descending)
        for i in range(M):
            flavor_customers[i].sort(reverse=True)
        
        # Now process the customers in order
        # We'll keep track of the flavor choices
        flavor_choices = []
        total_profit = 0
        
        for i in range(N):
            D_i = flavor_customers[i][0][0]  # D_i is the favorite flavor of the i-th customer
            # Check if we can serve the favorite flavor
            if flavor_available[D_i] > 0:
                # Serve the favorite flavor
                total_profit += flavor_customers[i][0][0]
                flavor_available[D_i] -= 1
                flavor_choices.append(D_i + 1)  # convert back to 1-based
            else:
                # Can't serve the favorite, so choose the best B_i from other flavors
                # We need to find the flavor with the highest B_i that still has availability
                # We'll collect all available flavors and pick the one with the highest B_i
                available_flavors = []
                for j in range(M):
                    if flavor_available[j] > 0:
                        # Get the best B_i for this flavor
                        best_b = flavor_b_heap[j][0][1]
                        available_flavors.append((best_b, j))
                # Sort available flavors by B_i (descending)
                available_flavors.sort(reverse=True)
                # Choose the flavor with the highest B_i
                best_b, best_flavor = available_flavors[0]
                total_profit += best_b
                flavor_available[best_flavor] -= 1
                flavor_choices.append(best_flavor + 1)
        
        results.append(str(total_profit))
        results.append(' '.join(map(str, flavor_choices)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()