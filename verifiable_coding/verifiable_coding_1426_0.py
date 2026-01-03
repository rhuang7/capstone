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
        # For each flavor, store the list of (F_i, B_i, customer index)
        flavor_customers = [[] for _ in range(M)]
        
        for i in range(N):
            D_i = int(data[idx]) - 1
            F_i = int(data[idx+1])
            B_i = int(data[idx+2])
            idx += 3
            flavor_customers[D_i].append((F_i, B_i, i))
        
        # For each flavor, sort customers by F_i in descending order
        for i in range(M):
            flavor_customers[i].sort(reverse=True)
        
        # For each flavor, keep a heap of (B_i, customer index)
        flavor_bheap = [[] for _ in range(M)]
        for i in range(M):
            for f, b, idx_c in flavor_customers[i]:
                heapq.heappush(flavor_bheap[i], (b, idx_c))
        
        # Process customers in order
        profit = 0
        flavor_choices = [0] * N
        
        for i in range(N):
            D_i = int(data[idx]) - 1
            F_i = int(data[idx+1])
            B_i = int(data[idx+2])
            idx += 3
            
            # Check if we can give the favorite flavor
            if flavor_available[D_i] > 0:
                profit += F_i
                flavor_choices[i] = D_i + 1
                flavor_available[D_i] -= 1
            else:
                # Choose the best possible flavor with available capacity
                # Find the flavor with the highest B_i among available ones
                max_b = -1
                best_flavor = -1
                best_idx = -1
                for j in range(M):
                    if flavor_available[j] > 0:
                        b, idx_c = flavor_bheap[j][0]
                        if b > max_b:
                            max_b = b
                            best_flavor = j
                            best_idx = idx_c
                if best_flavor != -1:
                    profit += max_b
                    flavor_choices[i] = best_flavor + 1
                    # Remove the best B_i from the heap
                    heapq.heappop(flavor_bheap[best_flavor])
                    flavor_available[best_flavor] -= 1
        
        results.append(str(profit))
        results.append(' '.join(map(str, flavor_choices)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()