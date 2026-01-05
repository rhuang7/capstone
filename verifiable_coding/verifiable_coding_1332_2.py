import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    queries = []
    idx = 1
    for _ in range(N):
        i = int(data[idx])
        j = int(data[idx+1])
        queries.append((i, j))
        idx += 2

    def get_depth(x):
        depth = 0
        while x > 1:
            x >>= 1
            depth += 1
        return depth

    def get_lca(a, b):
        depth_a = get_depth(a)
        depth_b = get_depth(b)
        if depth_a < depth_b:
            a, b = b, a
        # Bring a to the same depth as b
        for _ in range(depth_a - depth_b):
            a >>= 1
        if a == b:
            return a
        # Move both up until LCA is found
        while a != b:
            a >>= 1
            b >>= 1
        return a

    def get_distance(a, b):
        lca = get_lca(a, b)
        return get_depth(a) + get_depth(b) - 2 * get_depth(lca)

    for i, j in queries:
        print(get_distance(i, j))

if __name__ == '__main__':
    solve()