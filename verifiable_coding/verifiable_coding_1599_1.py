import sys
import collections

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
        idx += 1
        adj = collections.defaultdict(list)
        for _ in range(N-1):
            A = int(data[idx]) - 1
            B = int(data[idx+1]) - 1
            adj[A].append(B)
            adj[B].append(A)
            idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute parity of the number of bits
        # For each node, compute the parity of the number of set bits in a[i]
        # Also compute the parity of the distance from the root (0)
        # We'll use BFS to compute the parity of the distance from root
        # The parity of the distance is the parity of the number of edges in the path
        # So, for each node, we'll store the parity of the distance from root (0)
        
        # BFS to compute parity of distance from root
        visited = [False] * N
        queue = collections.deque()
        queue.append(0)
        visited[0] = True
        dist_parity = [0] * N
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist_parity[v] = dist_parity[u] ^ 1
                    queue.append(v)
        
        # For each node, compute the parity of the number of set bits in a[i]
        bit_parity = [bin(x).count('1') % 2 for x in a]
        
        # Now, for each pair (i, j), check if (bit_parity[i] ^ bit_parity[j]) == dist_parity[i] ^ dist_parity[j]
        # Count the number of such pairs
        count = 0
        for i in range(N):
            for j in range(N):
                if (bit_parity[i] ^ bit_parity[j]) == (dist_parity[i] ^ dist_parity[j]):
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)