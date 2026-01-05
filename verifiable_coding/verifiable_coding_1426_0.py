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
        customers = []
        for _ in range(N):
            D = int(data[idx])
            F = int(data[idx+1])
            B = int(data[idx+2])
            idx += 3
            customers.append((D, F, B))
        # Initialize flavor availability
        flavor_available = [True] * M
        # For each flavor, keep a list of (B_i, D_i) for customers who prefer it
        flavor_customers = [[] for _ in range(M)]
        # For other flavors, keep a max heap of (B_i, D_i)
        other_flavors = [[] for _ in range(M)]
        for i in range(N):
            D, F, B = customers[i]
            flavor_customers[D-1].append((F, B, i))
            # For other flavors, add (B, D, i) to the heap
            if D-1 != i:
                other_flavors[i].append((B, D, i))
        # Sort each flavor's customers by F in descending order
        for i in range(M):
            flavor_customers[i].sort(reverse=True)
        # For other flavors, create a max heap (using negative B)
        for i in range(M):
            other_flavors[i] = [(-b, d, i) for b, d, i in other_flavors[i]]
            heapq.heapify(other_flavors[i])
        # Process customers
        profit = 0
        flavor_used = [0] * M
        result = []
        for i in range(N):
            D, F, B = customers[i]
            # Check if we can give the favorite flavor
            if flavor_available[D-1]:
                # We can give the favorite flavor
                profit += F
                flavor_used[D-1] += 1
                flavor_available[D-1] = False
                result.append(D)
            else:
                # We need to choose another flavor
                # Try to find the best available flavor
                best_b = -1
                best_d = -1
                best_idx = -1
                # Check all flavors except D
                for j in range(M):
                    if j == D-1:
                        continue
                    if flavor_used[j] < C[j]:
                        # This flavor is available
                        if best_b < other_flavors[j][0][0]:
                            best_b = other_flavors[j][0][0]
                            best_d = other_flavors[j][0][1]
                            best_idx = j
                # If found, take the best
                if best_idx != -1:
                    profit += -best_b
                    flavor_used[best_idx] += 1
                    result.append(best_d)
                else:
                    # No other flavor available, but the problem says it's always possible
                    # So this shouldn't happen
                    pass
        results.append(profit)
        results.append(' '.join(map(str, result)))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()