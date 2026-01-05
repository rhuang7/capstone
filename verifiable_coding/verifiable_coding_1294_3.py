import sys
import math
from sys import stdin
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            edges[u].append(v)
            edges[v].append(u)
            idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Build tree
        visited = [False]*(N+1)
        tree = [[] for _ in range(N+1)]
        def dfs(u, parent):
            visited[u] = True
            for v in edges[u]:
                if not visited[v]:
                    tree[u].append(v)
                    dfs(v, u)
        dfs(1, -1)
        
        # Find all leaves
        leaves = []
        for i in range(1, N+1):
            if len(tree[i]) == 0:
                leaves.append(i)
        
        # For each leaf, check if it's possible to get K
        possible = False
        for leaf in leaves:
            # Get path from root to leaf
            path = []
            u = leaf
            while u != -1:
                path.append(u)
                u = parent[u]
            path.reverse()
            
            # Check if it's possible to get K with this path
            # For each node in path, choose D in [2^(A[i]-1), 2^A[i})
            # We need to find if there's a way to choose D's such that XOR or AND of all D's is K
            # Let's try both operations
            
            # Try XOR
            xor_possible = False
            # We can choose D_i as 2^(A[i]-1) or 2^A[i)-1, since those are the minimal and maximal possible values
            # Let's try choosing D_i as 2^(A[i]-1) for all, and see if XOR is K
            # If not, try some other combination
            # But since the range is [2^(A[i]-1), 2^A[i}), we can choose D_i as 2^(A[i]-1) or 2^A[i)-1
            # Let's try all combinations of choosing D_i as 2^(A[i]-1) or 2^A[i)-1
            # But since A[i] can be up to 64, this is not feasible for large paths
            # So we need a smarter way
            
            # Instead, let's try to find the XOR of all D_i's and see if it can be K
            # Since D_i can be any value in the range, we can choose D_i to be 2^(A[i]-1) or 2^A[i)-1
            # So the XOR can be any value that is a combination of these bits
            # Let's try to find the XOR of all D_i's as K
            # We can try to find if there's a way to choose D_i's such that their XOR is K
            # Let's try to find the minimal and maximal possible XOR values
            # For each node, the D_i can be in [2^(A[i]-1), 2^A[i})
            # So the minimal XOR is the XOR of all 2^(A[i]-1)
            # The maximal XOR is the XOR of all (2^A[i]-1)
            # If K is not in this range, it's impossible
            # But since the XOR can be any value in the range, we need to check if K can be formed
            
            # Let's compute the XOR of all 2^(A[i]-1)
            xor_min = 0
            for u in path:
                xor_min ^= (1 << (A[u-1]-1))
            
            # Let's compute the XOR of all (2^A[i]-1)
            xor_max = 0
            for u in path:
                xor_max ^= ((1 << A[u-1]) - 1)
            
            if xor_min <= K <= xor_max:
                possible = True
                break
            
            # Try AND
            and_possible = False
            # The AND of all D_i's must be K
            # Since D_i can be any value in the range [2^(A[i]-1), 2^A[i})
            # The AND of all D_i's must be K
            # Let's compute the AND of all 2^(A[i]-1)
            and_min = (1 << (A[path[0]-1]-1))
            for u in path[1:]:
                and_min &= (1 << (A[u-1]-1))
            
            # The AND of all (2^A[i]-1)
            and_max = (1 << (A[path[0]-1]-1))
            for u in path[1:]:
                and_max &= ((1 << A[u-1]) - 1)
            
            if and_min <= K <= and_max:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()