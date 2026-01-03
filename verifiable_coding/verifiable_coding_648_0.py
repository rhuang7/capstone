import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N

    from collections import defaultdict
    tree = [defaultdict(int) for _ in range(N+2)]
    def update(pos, val):
        while pos <= N:
            tree[pos][val] += 1
            pos += pos & -pos

    def query(pos):
        res = []
        while pos > 0:
            res.append(tree[pos])
            pos -= pos & -pos
        return res

    def get_next(pos):
        next_pos = pos + 1
        while next_pos <= N:
            if A[next_pos - 1] > A[pos - 1]:
                return next_pos
            next_pos += 1
        return pos

    def jump(i, k):
        current = i
        for _ in range(k):
            next_pos = get_next(current)
            if next_pos == current:
                return current
            current = next_pos
        return current

    for _ in range(Q):
        op = int(data[idx])
        idx += 1
        if op == 1:
            i = int(data[idx])
            idx += 1
            k = int(data[idx])
            idx += 1
            print(jump(i, k))
        else:
            L = int(data[idx])
            idx += 1
            R = int(data[idx])
            idx += 1
            X = int(data[idx])
            idx += 1
            for j in range(L-1, R):
                A[j] += X
                update(j+1, A[j])

if __name__ == '__main__':
    solve()