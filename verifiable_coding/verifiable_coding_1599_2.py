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
        
        # Precompute parity of the number of bits differing
        # For each pair (i, j), compute the parity of the bit difference
        # Also precompute the parity of the distance between i and j
        # But since the tree is undirected and connected, we can use BFS to find distances
        # However, for large N (up to 1e5), we need an efficient way to compute distances for all pairs
        # Instead, we can precompute the parity of the distance between all pairs
        
        # Precompute parity of distance between all pairs
        # Using BFS for each node
        # But for N=1e5, this is O(N^2), which is not feasible
        # So we need a better approach
        
        # Since the tree is undirected and connected, we can use BFS to find the parity of the distance between all pairs
        # But again, for N=1e5, this is not feasible
        
        # Alternative approach: Since the parity of the distance between two nodes is equal to the parity of the number of edges in the path between them
        # Which is the same as the parity of the depth of the two nodes in a BFS tree
        # So we can root the tree at an arbitrary node and compute the depth of each node
        # Then, the parity of the distance between two nodes is (depth[u] + depth[v]) % 2
        
        # So we can root the tree at node 0 and compute the depth of each node
        # Then, for each pair (u, v), the parity of the distance is (depth[u] + depth[v]) % 2
        
        # So we can precompute the depth of each node
        # Then, for each pair (u, v), the parity of the bit difference between a[u] and a[v] is (bit_diff_parity[u][v]) % 2
        # And the parity of the distance is (depth[u] + depth[v]) % 2
        
        # So we need to compute for all pairs (u, v) whether (bit_diff_parity[u][v] % 2) == ((depth[u] + depth[v]) % 2)
        
        # But for N=1e5, we cannot check all pairs
        
        # So we need to find a way to count the number of pairs (u, v) such that:
        # (bit_diff_parity[u][v] % 2) == ((depth[u] + depth[v]) % 2)
        
        # Let's precompute the parity of the bit difference between a[u] and a[v] for all pairs (u, v)
        # But again, this is O(N^2), which is not feasible
        
        # So we need to find a way to compute this efficiently
        
        # Let's think about the parity of the bit difference between a[u] and a[v]
        # This is equal to the parity of the XOR of a[u] and a[v]
        # Because XOR gives 1 for each differing bit
        # So the number of differing bits is the Hamming weight of (a[u] ^ a[v])
        # The parity is the sum of the bits modulo 2
        
        # So the parity of the bit difference is (a[u] ^ a[v]).bit_count() % 2
        # Which is equal to (a[u] ^ a[v]) & 1
        
        # So we can precompute for each node u, the parity of a[u] (a[u] & 1)
        # Then, for any pair (u, v), the parity of the bit difference is (parity_u ^ parity_v)
        
        # So the condition becomes:
        # (parity_u ^ parity_v) == ((depth[u] + depth[v]) % 2)
        
        # So we can group nodes by their parity and depth parity
        
        # Let's compute for each node u:
        # parity_u = a[u] & 1
        # depth_parity_u = depth[u] % 2
        
        # Now, for all pairs (u, v), we need to count the number of pairs where:
        # (parity_u ^ parity_v) == (depth_parity_u + depth_parity_v) % 2
        
        # Let's precompute the depth of each node using BFS
        # Then, compute the parity of the depth for each node
        # Then, group nodes by (parity_u, depth_parity_u)
        
        # So the total number of valid pairs is:
        # count[(parity_u, depth_parity_u)] * count[(parity_v, depth_parity_v)] for all pairs (u, v)
        # But we need to ensure that (parity_u ^ parity_v) == (depth_parity_u + depth_parity_v) % 2
        
        # Let's compute this
        
        # First, compute depth of each node using BFS
        depth = [0] * N
        visited = [False] * N
        queue = collections.deque()
        queue.append(0)
        visited[0] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    queue.append(v)
        
        # Now, compute parity of depth for each node
        depth_parity = [depth[i] % 2 for i in range(N)]
        
        # Compute parity of a[i] for each node
        parity = [a[i] & 1 for i in range(N)]
        
        # Now, group nodes by (parity[i], depth_parity[i])
        count = collections.defaultdict(int)
        for i in range(N):
            count[(parity[i], depth_parity[i])] += 1
        
        # Now, for each possible pair of (p1, d1) and (p2, d2), check if (p1 ^ p2) == (d1 + d2) % 2
        # If yes, then the number of pairs is count[(p1, d1)] * count[(p2, d2)]
        # But since (p1, d1) and (p2, d2) are considered in all combinations, we need to avoid double counting
        # So we can iterate over all possible combinations of (p1, d1) and (p2, d2) where (p1 ^ p2) == (d1 + d2) % 2
        # And sum count[(p1, d1)] * count[(p2, d2)]
        
        total = 0
        for (p1, d1), cnt1 in count.items():
            for (p2, d2), cnt2 in count.items():
                if (p1 ^ p2) == (d1 + d2) % 2:
                    total += cnt1 * cnt2
        
        # Since each pair (u, v) is counted twice (once as (u, v) and once as (v, u)), we need to divide by 2
        # But we also need to include the cases where u == v
        # So we need to subtract the cases where u == v and then add them back
        # But since the problem allows u == v, we need to handle that correctly
        
        # However, the current approach counts all pairs (u, v) including u == v
        # But the condition (p1 ^ p2) == (d1 + d2) % 2 is symmetric, so the total is correct
        
        # But the current approach counts (u, v) and (v, u) as two separate pairs, but they are the same
        # So we need to divide by 2 and then add the number of valid (u, u) pairs
        
        # So let's compute the total correctly
        # First, compute the total number of pairs (u, v) where u != v and the condition is satisfied
        # Then, add the number of valid (u, u) pairs
        
        # So let's compute the total as follows:
        # total = 0
        # for (p1, d1), cnt1 in count.items():
        #     for (p2, d2), cnt2 in count.items():
        #         if (p1 ^ p2) == (d1 + d2) % 2:
        #             if p1 == p2 and d1 == d2:
        #                 total += cnt1 * (cnt1 - 1)
        #             else:
        #                 total += cnt1 * cnt2
        
        # But this is not correct, because we are