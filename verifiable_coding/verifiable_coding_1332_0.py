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

    def get_ancestors(x):
        ancestors = set()
        while x > 0:
            ancestors.add(x)
            x = x // 2
        return ancestors

    for i, j in queries:
        ancestors_i = get_ancestors(i)
        ancestors_j = get_ancestors(j)
        common = ancestors_i & ancestors_j
        if not common:
            print(0)
            continue
        common = max(common)
        depth_i = i.bit_length() - 1
        depth_j = j.bit_length() - 1
        depth_common = common.bit_length() - 1
        distance = (depth_i - depth_common) + (depth_j - depth_common)
        print(distance)

if __name__ == '__main__':
    solve()