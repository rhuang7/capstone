import sys
import collections

def solve():
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
        
        # Precompute parity of the number of bits differing
        # For each pair (i, j), compute the parity of the XOR of a[i] and a[j]
        # Also compute the parity of the distance between i and j
        # The condition is that the parity of the XOR is equal to the parity of the distance
        
        # Precompute the parity of the distance between all pairs
        # Using BFS for each node
        def bfs(start):
            dist = [-1] * N
            q = collections.deque()
            q.append(start)
            dist[start] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist
        
        parities = []
        for i in range(N):
            parities.append(bfs(i))
        
        # Now, for each pair (i, j), check if the parity of the XOR of a[i] and a[j] is equal to the parity of the distance between i and j
        count = 0
        for i in range(N):
            for j in range(N):
                xor_parity = bin(a[i] ^ a[j]).count('1') % 2
                dist_parity = parities[i][j] % 2
                if xor_parity == dist_parity:
                    count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()