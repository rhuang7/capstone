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
        
        # Try all leaves
        possible = False
        for leaf in leaves:
            path = []
            u = leaf
            while u != 1:
                path.append(u)
                u = 1
                # Find path from leaf to root
                while u != 1:
                    for v in tree[u]:
                        if v != 1:
                            u = v
                            break
            path.append(1)
            path.reverse()
            
            # Check if we can choose D values for this path
            # such that XOR or AND gives K
            # Try XOR
            xor_val = 0
            for i in path:
                a = A[i-1]
                low = 1 << (a-1)
                high = (1 << a)
                # Choose D in [low, high)
                # For XOR, we need to find a value that can contribute to K
                # Try all possible D in [low, high)
                # But since a can be up to 64, we can't try all possibilities
                # So we need a smarter way
                # For XOR, we can try to set bits in D to match K
                # For AND, we need all D to have certain bits set
                # Let's try both possibilities
                # Try XOR
                # Try to find a D for this node that can help reach K
                # For XOR, we can try to set D to match K's bits
                # But since D must be in [low, high), we can try to set D to be the same as K
                # But K may not be in that range
                # So we can try to set D to be the same as K if possible
                # Otherwise, try to set D to the minimum or maximum in the range
                # Try D = K if it is in the range
                if low <= K < high:
                    xor_val ^= K
                else:
                    # Try to set D to be the minimum in the range
                    d = low
                    xor_val ^= d
                # Try to set D to be the maximum in the range
                d = high - 1
                xor_val ^= d
            if xor_val == K:
                possible = True
                break
            # Try AND
            and_val = (1 << 64) - 1
            for i in path:
                a = A[i-1]
                low = 1 << (a-1)
                high = (1 << a)
                # For AND, all D must have certain bits set
                # So we need to choose D such that it has all bits set that are required for K
                # So we can try to set D to be the same as K if possible
                # Otherwise, try to set D to be the minimum or maximum in the range
                # Try D = K if it is in the range
                if low <= K < high:
                    and_val &= K
                else:
                    # Try to set D to be the minimum in the range
                    d = low
                    and_val &= d
                # Try to set D to be the maximum in the range
                d = high - 1
                and_val &= d
            if and_val == K:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))