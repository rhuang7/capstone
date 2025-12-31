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
        parity = [0] * N
        for i in range(N):
            parity[i] = bin(a[i]).count('1') % 2
        
        # Precompute distance between all pairs using BFS
        # Since it's a tree, we can do BFS from each node
        # But for large N (up to 1e5), this is O(N^2), which is not feasible
        # So we need a smarter approach
        
        # Instead, we can note that the parity of the distance between two nodes
        # is equal to the parity of the XOR of their depths in a BFS tree
        # So we can root the tree and compute depths for each node
        # Then, for each node, we can count the number of nodes with the same parity of depth
        # and the number of nodes with different parity of depth
        
        # Let's root the tree at node 0
        depth = [0] * N
        visited = [False] * N
        queue = collections.deque([0])
        visited[0] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    queue.append(v)
        
        # Count parity of depth
        even_depth = 0
        odd_depth = 0
        for i in range(N):
            if depth[i] % 2 == 0:
                even_depth += 1
            else:
                odd_depth += 1
        
        # Now, for each node, we need to count the number of nodes where:
        # (parity of a_i XOR parity of a_j) == (parity of distance between i and j)
        # Which is equivalent to:
        # (parity of a_i XOR parity of a_j) == (parity of (depth[i] XOR depth[j]))
        
        # Let's precompute the parity of a_i
        a_parity = [bin(a[i]).count('1') % 2 for i in range(N)]
        
        # Now, we can count the number of pairs (i, j) where:
        # (a_parity[i] XOR a_parity[j]) == (depth[i] XOR depth[j]) % 2
        
        # Let's count the number of nodes with each combination of a_parity and depth_parity
        count = [0] * 4
        for i in range(N):
            dp = depth[i] % 2
            ap = a_parity[i]
            count[ap * 2 + dp] += 1
        
        # Now, for each pair (x, y), if (x XOR y) == (x XOR y), then it's valid
        # So for each pair (x, y), if (x XOR y) == (x XOR y), then it's valid
        # Which is always true, so all pairs are valid
        # Wait, no. We need (a_parity[i] XOR a_parity[j]) == (depth[i] XOR depth[j]) % 2
        
        # So, for each pair (i, j), the condition is:
        # (a_parity[i] XOR a_parity[j]) == (depth[i] XOR depth[j]) % 2
        
        # Let's count the number of valid pairs
        total = 0
        for i in range(N):
            for j in range(N):
                if (a_parity[i] ^ a_parity[j]) == (depth[i] ^ depth[j]) % 2:
                    total += 1
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()