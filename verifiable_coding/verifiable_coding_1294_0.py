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
        
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Build the tree with parent pointers
        parent = [0]*(N+1)
        visited = [False]*(N+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v] and v != parent[u]:
                    parent[v] = u
                    visited[v] = True
                    q.append(v)
        
        # Find all leaves
        leaves = []
        for i in range(1, N+1):
            if len(tree[i]) == 1 and i != 1:
                leaves.append(i)
        
        # Try each leaf
        possible = False
        for leaf in leaves:
            path = []
            u = leaf
            while u != 1:
                path.append(u)
                u = parent[u]
            path.append(1)
            path.reverse()
            
            # Check if we can get K by XOR or AND
            # For each node in path, choose D in [2^(A[i]-1), 2^A[i})
            # We need to find if there exists a choice of D's such that XOR or AND of all D's is K
            
            # Try XOR
            xor = 0
            for i in path:
                a = A[i-1]
                low = 1 << (a-1)
                high = (1 << a)
                # Try all possible D in [low, high)
                # But since we need to find if any choice works, we can try the minimal and maximal values
                # Because any D in that range will have the same bit pattern for the highest bit
                # So we can try the minimal and maximal values for each node
                # Try minimal value
                d_min = low
                xor_min = xor ^ d_min
                # Try maximal value
                d_max = high - 1
                xor_max = xor ^ d_max
                # Update xor to the minimal possible value
                xor = xor_min
                # If at any point, the xor becomes K, we can return True
                if xor == K:
                    possible = True
                    break
                # If we have tried all possibilities and not found K, try the other path
                # But since we are trying minimal and maximal, we can just try one of them
                # So we can just try the minimal value for each node
            if possible:
                break
            # Try AND
            and_val = (1 << 64) - 1
            for i in path:
                a = A[i-1]
                low = 1 << (a-1)
                high = (1 << a)
                # Try all possible D in [low, high)
                # But since we need to find if any choice works, we can try the minimal and maximal values
                # For AND, we need to find if there exists a choice of D's such that AND of all D's is K
                # Try minimal value
                d_min = low
                and_val_min = and_val & d_min
                # Try maximal value
                d_max = high - 1
                and_val_max = and_val & d_max
                # Update and_val to the minimal possible value
                and_val = and_val_min
                # If at any point, the and_val becomes K, we can return True
                if and_val == K:
                    possible = True
                    break
            if possible:
                break
        
        results.append("YES" if possible else "NO")
    
    print('\n'.join(results))