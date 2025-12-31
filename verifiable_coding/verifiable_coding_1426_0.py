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
        D = []
        F = []
        B = []
        for _ in range(N):
            d = int(data[idx])
            f = int(data[idx+1])
            b = int(data[idx+2])
            D.append(d - 1)  # 0-based
            F.append(f)
            B.append(b)
            idx += 3
        # Initialize available flavors
        available = [i for i in range(M)]
        # For each flavor, keep a priority queue of (B_i, F_i, D_i)
        # We'll use a max-heap for B_i, but since Python has min-heap, we'll use negative B_i
        flavor_pq = [[] for _ in range(M)]
        for i in range(N):
            d = D[i]
            f = F[i]
            b = B[i]
            heapq.heappush(flavor_pq[d], (-b, -f, i))
        # Track the number of available flavors for each flavor
        count = [0] * M
        # Track the chosen flavor for each customer
        chosen = [0] * N
        # Track the profit
        profit = 0
        # Process each customer
        for i in range(N):
            d = D[i]
            # Check if we can satisfy the customer's favorite flavor
            if count[d] < C[d]:
                # We can give the favorite flavor
                profit += F[i]
                chosen[i] = d + 1  # 1-based
                count[d] += 1
            else:
                # We need to choose another flavor
                # Find the flavor with the highest B_i (or F_i if B_i is same)
                max_b = -1
                max_f = -1
                best_flavor = -1
                for j in range(M):
                    if count[j] < C[j]:
                        b, f, _ = flavor_pq[j][0] if flavor_pq[j] else (0, 0, 0)
                        b = -b
                        f = -f
                        if b > max_b or (b == max_b and f > max_f):
                            max_b = b
                            max_f = f
                            best_flavor = j
                if best_flavor != -1:
                    # Take the best available flavor
                    profit += max_b
                    chosen[i] = best_flavor + 1
                    count[best_flavor] += 1
                    # Remove the best flavor from the heap
                    heapq.heappop(flavor_pq[best_flavor])
                    # Push the next best flavor for this flavor
                    if flavor_pq[best_flavor]:
                        b, f, _ = flavor_pq[best_flavor][0]
                        b = -b
                        f = -f
                        heapq.heappush(flavor_pq[best_flavor], (-b, -f, i))
        results.append(str(profit))
        results.append(' '.join(map(str, chosen)))
    print('\n'.join(results))