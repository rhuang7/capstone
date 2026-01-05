import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
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
        tree = [[] for _ in range(N+1)]
        visited = [False] * (N+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    tree[u].append(v)
                    q.append(v)
        
        # Find leaves
        leaves = []
        for i in range(1, N+1):
            if len(tree[i]) == 0:
                leaves.append(i)
        
        # For each leaf, find the path from root to leaf
        possible = False
        for leaf in leaves:
            path = []
            u = leaf
            while u != 1:
                path.append(u)
                u = 1
                # Find parent of u
                for v in tree[u]:
                    if v != 1:
                        u = v
                        break
            path.append(1)
            path = path[::-1]
            
            # Check if we can choose D values such that XOR or AND equals K
            # For each node in path, D is in [2^{A[i]-1}, 2^{A[i}})
            # We can represent D as a binary number with exactly A[i] bits, where the first bit is 1
            # So for each node, the D can be any number with exactly A[i] bits, starting with 1
            
            # Try XOR
            xor_val = 0
            for i in path:
                a = A[i-1]
                # The D can be any number in [2^{a-1}, 2^a)
                # So the minimum is 2^{a-1}, maximum is 2^a - 1
                # We can choose D as 2^{a-1} (which is 1 followed by a-1 zeros)
                # So for XOR, we can try to set D as 2^{a-1}
                xor_val ^= (1 << (a-1))
            
            if xor_val == K:
                possible = True
                break
            
            # Try AND
            and_val = (1 << 64) - 1
            for i in path:
                a = A[i-1]
                # The D can be any number in [2^{a-1}, 2^a)
                # The AND of all D's will be at least 2^{a-1} for each a
                # So the AND is at least the minimum of all 2^{a-1}
                and_val &= (1 << (a-1))
            
            if and_val == K:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()