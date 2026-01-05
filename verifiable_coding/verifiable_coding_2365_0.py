import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        # Build a graph where each node is a number and edges represent possible positions
        # We'll use a union-find structure to group numbers that must be in the same segment
        parent = list(range(n+1))
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parent[pv] = pu
        # For each segment, merge all elements together
        for seg in segments:
            for i in range(1, len(seg)):
                union(seg[i-1], seg[i])
        # Now, the permutation must be such that each number is in the correct position
        # We can construct the permutation by placing the smallest number in the earliest position
        # that is not yet occupied
        p = [0] * (n + 1)
        used = [False] * (n + 1)
        for i in range(1, n+1):
            # Find the root of i
            root = find(i)
            # Find the smallest number in the connected component of root
            min_val = None
            for j in range(1, n+1):
                if find(j) == root and (min_val is None or j < min_val):
                    min_val = j
            # Place min_val in the first available position
            for pos in range(1, n+1):
                if not used[pos]:
                    p[pos] = min_val
                    used[pos] = True
                    break
        results.append(' '.join(map(str, p[1:])))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()