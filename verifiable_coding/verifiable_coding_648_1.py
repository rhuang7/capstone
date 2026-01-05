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

    # Preprocess next greater element for each position
    next_greater = [0] * (N + 2)  # 1-based indexing
    for i in range(N-1, -1, -1):
        # Find next strictly greater element within 100 distance
        for j in range(i+1, min(i+101, N)):
            if A[j] > A[i]:
                next_greater[i] = j
                break
        else:
            next_greater[i] = i

    # For type 2 operations, we need to support range updates
    # We'll use a segment tree with lazy propagation
    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            self.tree = [0] * (4 * self.n)
            self.lazy = [0] * (4 * self.n)
            self.build(1, 0, self.n - 1, data)

        def build(self, node, l, r, data):
            if l == r:
                self.tree[node] = data[l]
                return
            mid = (l + r) // 2
            self.build(2*node, l, mid, data)
            self.build(2*node+1, mid+1, r, data)
            self.tree[node] = data[l]

        def push(self, node, l, r):
            if self.lazy[node] != 0:
                self.tree[node] += self.lazy[node]
                if l != r:
                    self.lazy[2*node] += self.lazy[node]
                    self.lazy[2*node+1] += self.lazy[node]
                self.lazy[node] = 0

        def range_update(self, node, l, r, ul, ur, val):
            self.push(node, l, r)
            if ur < l or ul > r:
                return
            if ul <= l and r <= ur:
                self.lazy[node] += val
                self.push(node, l, r)
                return
            mid = (l + r) // 2
            self.range_update(2*node, l, mid, ul, ur, val)
            self.range_update(2*node+1, mid+1, r, ul, ur, val)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

        def query(self, node, l, r, ql, qr):
            self.push(node, l, r)
            if qr < l or ql > r:
                return 0
            if ql <= l and r <= qr:
                return self.tree[node]
            mid = (l + r) // 2
            left = self.query(2*node, l, mid, ql, qr)
            right = self.query(2*node+1, mid+1, r, ql, qr)
            return left + right

    st = SegmentTree(A)

    def get_val(i):
        return st.query(1, 0, N-1, i-1, i-1)

    for _ in range(Q):
        op = int(data[idx])
        idx += 1
        if op == 1:
            i = int(data[idx]) - 1
            idx += 1
            k = int(data[idx])
            idx += 1
            current = i
            for _ in range(k):
                next_g = next_greater[current]
                if next_g == current:
                    break
                current = next_g
            print(current + 1)
        else:
            L = int(data[idx]) - 1
            idx += 1
            R = int(data[idx]) - 1
            idx += 1
            X = int(data[idx])
            idx += 1
            st.range_update(1, 0, N-1, L, R, X)