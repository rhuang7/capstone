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
        # For each pair (i, j), compute the parity of the bit difference
        # Also precompute the parity of the distance between i and j
        # But since the tree is undirected and connected, we can use BFS to compute distances
        
        # Precompute distance parity for all pairs
        # Since N can be up to 1e5, O(N^2) is not feasible
        # So we need a way to compute for each node, the parity of the distance to all other nodes
        # This can be done with BFS for each node, but that would be O(N^2), which is too slow
        
        # Alternative approach: Since the tree is undirected and connected, the parity of the distance between two nodes is equal to the parity of the XOR of their depths in a BFS traversal
        # So we can do a BFS from an arbitrary root, compute the depth of each node, and then the parity of the distance between two nodes is (depth[u] + depth[v]) % 2
        
        # So we need to compute the depth of each node from an arbitrary root (say 0)
        # Then, for each pair (u, v), the parity of the distance is (depth[u] + depth[v]) % 2
        
        # Now, for each pair (u, v), we need to check if the parity of the bit difference between a[u] and a[v] is equal to the parity of the distance between u and v
        
        # So, for each pair (u, v), compute:
        # bit_diff_parity = (bin(a[u] ^ a[v]).count('1') % 2)
        # distance_parity = (depth[u] + depth[v]) % 2
        # if bit_diff_parity == distance_parity, count it
        
        # So we need to:
        # 1. Compute depth of each node
        # 2. For each pair (u, v), compute bit_diff_parity and distance_parity
        # 3. Count the number of pairs where they are equal
        
        # Compute depth using BFS
        depth = [0] * N
        visited = [False] * N
        q = collections.deque()
        q.append(0)
        visited[0] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Precompute the bit difference parity for all pairs
        # But since N is up to 1e5, O(N^2) is not feasible
        # So we need to find a way to count the number of pairs (u, v) where (bit_diff_parity == distance_parity)
        
        # Let's precompute for each node u, the number of nodes v where:
        # (bit_diff_parity of a[u] and a[v] == (depth[u] + depth[v]) % 2)
        
        # For each u, we can iterate through all v and check the condition
        # But this is O(N^2), which is not feasible for N=1e5
        
        # So we need to find a way to group nodes based on their a[i] and depth[i]
        
        # Let's precompute for each node u, the parity of a[u] (bit_diff_parity for a[u] and a[v] depends on a[u] ^ a[v])
        # So for each node u, we can precompute the parity of a[u]
        # Then, for each node v, the parity of a[u] ^ a[v] is (parity_u + parity_v) % 2
        
        # So the bit_diff_parity is (parity_u + parity_v) % 2
        # The distance_parity is (depth_u + depth_v) % 2
        # So we need (parity_u + parity_v) % 2 == (depth_u + depth_v) % 2
        # Which simplifies to (parity_u - depth_u) % 2 == (parity_v - depth_v) % 2
        
        # So for each node, compute (parity_a - depth) % 2
        # Then, the number of pairs (u, v) where this value is the same is the count
        
        # So we can group nodes by this value and compute the count of pairs
        
        # Compute (parity_a - depth) % 2 for each node
        parity_a = [bin(x).count('1') % 2 for x in a]
        key = [(parity_a[i] - depth[i]) % 2 for i in range(N)]
        
        # Count frequency of each key
        freq = collections.defaultdict(int)
        for k in key:
            freq[k] += 1
        
        # The number of valid pairs is sum(freq[k] * (freq[k] - 1) // 2 for k in freq) + sum(freq[k] for k in freq)
        # Because for each pair (u, v), if they have the same key, then they are valid
        # Also, when u = v, it's valid if the parity of the bit difference is equal to the parity of the distance (which is 0)
        # So we need to count all pairs (u, v) where key[u] == key[v]
        
        total = 0
        for count in freq.values():
            total += count * (count - 1) // 2
            total += count
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()